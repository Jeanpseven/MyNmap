import subprocess
import sys
import datetime

def install_nmap():
    try:
        # Verifica se o Nmap está instalado
        subprocess.run(["nmap", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    except FileNotFoundError:
        print("Nmap não foi encontrado. Tentando instalar o Nmap...")

        package_managers = {
            "debian": ["sudo", "apt", "install", "nmap"],
            "redhat": ["sudo", "yum", "install", "nmap"],
            "arch": ["sudo", "pacman", "-Sy", "nmap"]
        }

        installed = False
        for distro, install_command in package_managers.items():
            if subprocess.run(["which", distro], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).returncode == 0:
                print(f"Detectado sistema baseado em {distro.capitalize()}. Instalando o Nmap...")
                subprocess.run(install_command)
                installed = True
                break

        if not installed:
            print("Não foi possível detectar o gerenciador de pacotes. Manualmente instale o Nmap.")

def run_nmap():
    print("Bem-vindo ao Nmap Wizard!")
    target = input("Digite o alvo da varredura (ex: 192.168.1.1): ")

    print("Escolha o tipo de varredura:")
    print("1. Varredura rápida de portas comuns")
    print("2. Varredura completa (pode levar mais tempo, inclui verificação de vulnerabilidades)")
    scan_type = input("Opção: ")

    if scan_type == "1":
        nmap_command = f"nmap -F -sV {target}"
    elif scan_type == "2":
        nmap_command = f"nmap -p- -sV --script=vulners {target}"
    else:
        print("Opção inválida. Saindo.")
        return

    log_file = f"nmap_scan_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

    print(f"Executando Nmap e salvando o log em '{log_file}'...")

    try:
        with open(log_file, 'w') as log:
            result = subprocess.run(nmap_command, shell=True, text=True, stdout=log, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o comando Nmap: {e}")
    else:
        print(f"Varredura concluída. Resultados salvos em '{log_file}'.")

if __name__ == "__main__":
    install_nmap()
    run_nmap()
