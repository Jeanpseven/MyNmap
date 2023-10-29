import subprocess
import sys
import datetime

def install_nikto():
    try:
        # Verifica se o Nikto está instalado
        subprocess.run(["nikto", "-Version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    except FileNotFoundError:
        print("Nikto não foi encontrado. Tentando instalar o Nikto...")

        try:
            # Tente instalar o Nikto usando o gerenciador de pacotes apropriado do sistema.
            # Os comandos a seguir são exemplos genéricos e podem variar dependendo do sistema.

            # Para sistemas baseados em Debian (como o Ubuntu):
            subprocess.run(["sudo", "apt", "update"])
            subprocess.run(["sudo", "apt", "install", "nikto"])

            # Para sistemas baseados em Red Hat (como o CentOS):
            subprocess.run(["sudo", "yum", "install", "nikto"])

            # Para sistemas baseados no Arch Linux:
            subprocess.run(["sudo", "pacman", "-Sy", "nikto"])

            # Você pode adicionar suporte a outros sistemas e gerenciadores de pacotes aqui.

        except Exception as e:
            print(f"Erro ao instalar o Nikto: {e}")
            sys.exit(1)

def run_nikto():
    print("Bem-vindo ao Nikto Wizard!")
    target = input("Digite o alvo da varredura (ex: http://exemplo.com): ")

    # Gere um nome de arquivo com a data e hora atual
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
    log_file = f"nikto_scan_{timestamp}.txt"

    nikto_command = f"nikto -h {target} -output {log_file}"

    print(f"Executando Nikto e salvando o log em '{log_file}'...")

    result = subprocess.run(nikto_command, shell=True, text=True)

    print(f"Varredura concluída. Resultados salvos em '{log_file}'.")

if __name__ == "__main__":
    install_nikto()
    run_nikto()