import os
import re

# Função para extrair CVEs do log e salvar em um arquivo TXT
def extract_and_save_cves(log_directory, output_file):
    cves = set()  # Usando um conjunto para evitar duplicatas

    # Verifica se o diretório existe
    if not os.path.exists(log_directory):
        print(f"O diretório '{log_directory}' não foi encontrado.")
        return

    # Lista os arquivos no diretório
    files = os.listdir(log_directory)

    # Procura por arquivos CSV no diretório
    csv_files = [file for file in files if file.endswith(".csv")]

    for csv_file in csv_files:
        # Constrói o caminho completo para o arquivo CSV
        csv_file_path = os.path.join(log_directory, csv_file)

        # Lê o conteúdo do arquivo CSV
        with open(csv_file_path, 'r', encoding='utf-8', errors='ignore') as log:
            log_content = log.read()

            # Use uma expressão regular para encontrar CVEs no log
            cve_pattern = r"CVE-\d{4}-\d{4,7}"
            cve_matches = re.findall(cve_pattern, log_content)

            # Adicione os CVEs encontrados ao conjunto
            cves.update(cve_matches)

    # Salve os CVEs em um arquivo TXT
    with open(output_file, 'w') as txt_file:
        for cve in cves:
            txt_file.write(cve + "\n")

    print(f"CVEs extraídos dos arquivos CSV e salvos em '{output_file}'.")

# Caminho para o diretório que contém os arquivos CSV
log_directory = "caminho/para/diretorio"

# Caminho para o arquivo TXT onde os CVEs serão salvos
output_file = "cves.txt"

# Chame a função para extrair e salvar os CVEs
extract_and_save_cves(log_directory, output_file)
