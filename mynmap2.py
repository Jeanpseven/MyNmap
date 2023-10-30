import subprocess
import sys
import datetime

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

    # Gere um nome de arquivo com a data e hora atual
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
    log_file = f"nmap_scan_{timestamp}.log"

    print(f"Executando Nmap e salvando o log em '{log_file}'...")

    # Redirecione a saída do Nmap para o arquivo de log
    with open(log_file, 'w') as log:
        result = subprocess.run(nmap_command, shell=True, text=True, stdout=log, stderr=log)

    print(f"Varredura concluída. Resultados salvos em '{log_file}'.")

if __name__ == "__main":
    install_nmap()
    run_nmap()