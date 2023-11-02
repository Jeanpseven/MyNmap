import subprocess
import sys
import datetime
import os
import csv

def install_sqlmap():
    try:
        # Verifica se o SQLMap está instalado
        subprocess.run(["sqlmap", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    except FileNotFoundError:
        print("SQLMap não foi encontrado. Tentando instalar o SQLMap...")

        try:
            # Tente instalar o SQLMap usando o gerenciador de pacotes apropriado do sistema.
            # Os comandos a seguir são exemplos genéricos e podem variar dependendo do sistema.

            # Para sistemas baseados em Debian (como o Ubuntu):
            subprocess.run(["sudo", "apt", "update"])
            subprocess.run(["sudo", "apt", "install", "sqlmap"])

            # Para sistemas baseados em Red Hat (como o CentOS):
            subprocess.run(["sudo", "yum", "install", "sqlmap"])

            # Para sistemas baseados no Arch Linux:
            subprocess.run(["sudo", "pacman", "-Sy", "sqlmap"])

            # Você pode adicionar suporte a outros sistemas e gerenciadores de pacotes aqui.

        except Exception as e:
            print(f"Erro ao instalar o SQLMap: {e}")
            sys.exit(1)

def run_sqlmap():
    print("Bem-vindo ao SQLMap Wizard!")
    target = input("Digite o alvo da varredura (ex: http://exemplo.com): ")

    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
    log_file = f"sqlmap_scan_{timestamp}.csv"

    sqlmap_command = f"sqlmap -u {target} --batch --output={log_file} --forms --crawl=2"

    print(f"Executando SQLMap e salvando o log em '{log_file}'...")

    result = subprocess.run(sqlmap_command, shell=True, text=True)

    print(f"Varredura concluída. Resultados salvos em '{log_file}'.")

    if os.path.isfile(log_file):
        with open(log_file, 'r', newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            
            headers = next(csv_reader)

            cves = []

            cve_column_index = None
            for i, header in enumerate(headers):
                if 'CVE' in header:
                    cve_column_index = i

            if cve_column_index is not None:
                for row in csv_reader:
                    cve = row[cve_column_index]
                    if cve:
                        cves.append(cve)

                if cves:
                    print("CVEs relacionados às vulnerabilidades encontradas:")
                    for cve in cves:
                        print(cve)
            else:
                print("Nenhuma coluna com CVEs foi encontrada no arquivo CSV.")

    else:
        print(f"Erro: '{log_file}' não é um arquivo válido.")

if __name__ == "__main__":
    install_sqlmap()
    run_sqlmap()
