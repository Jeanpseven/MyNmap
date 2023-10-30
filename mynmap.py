import subprocess
import sys
import requests

def install_nmap():
    try:
        # Verifica se o Nmap está instalado
        subprocess.run(["nmap", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    except FileNotFoundError:
        print("Nmap não foi encontrado. Tentando instalar o Nmap...")

        try:
            # Tente instalar o Nmap usando o gerenciador de pacotes apropriado do sistema.
            # Os comandos a seguir são exemplos genéricos e podem variar dependendo do sistema.

            # Para sistemas baseados em Debian (como o Ubuntu):
            subprocess.run(["sudo", "apt", "update"])
            subprocess.run(["sudo", "apt", "install", "nmap"])

            # Para sistemas baseados em Red Hat (como o CentOS):
            subprocess.run(["sudo", "yum", "install", "nmap"])

            # Para sistemas baseados no Arch Linux:
            subprocess.run(["sudo", "pacman", "-Sy", "nmap"])

            # Você pode adicionar suporte a outros sistemas e gerenciadores de pacotes aqui.

        except Exception as e:
            print(f"Erro ao instalar o Nmap: {e}")
            sys.exit(1)

def find_hidden_subdomains(target):
    try:
        response = requests.get(f"http://{target}")
        if response.status_code == 200:
            print(f"Headers HTTP do alvo {target}:\n")
            for header, value in response.headers.items():
                print(f"{header}: {value}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer a solicitação HTTP: {e}")

def run_nmap():
    print("Bem-vindo ao Nmap Wizard!")
    target = input("Digite o alvo da varredura (ex: 192.168.1.1): ")

    print("Escolha o tipo de varredura:")
    print("1. Varredura rápida de portas comuns")
    print("2. Varredura completa (leva mais tempo)")
    scan_type = input("Opção: ")

    if scan_type == "1":
        nmap_command = f"nmap -F -sV {target} --script vuln"
    elif scan_type == "2":
        nmap_command = f"nmap -p- -sV {target} --script vuln"
    else:
        print("Opção inválida. Saindo.")
        return

    print("Executando Nmap...")
    result = subprocess.run(nmap_command, shell=True, text=True, capture_output=True)

    print("Saída do Nmap:")
    print(result.stdout)

if __name__ == "__main__":
    install_nmap()
    run_nmap()
    find_hidden_subdomains(target)