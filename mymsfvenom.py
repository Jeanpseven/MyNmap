import subprocess

def check_msfvenom_installed():
    try:
        subprocess.run("msfvenom --version", shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

def install_msfvenom():
    try:
        print("Iniciando a instalação do msfvenom...")
        subprocess.run("apt-get install -y metasploit-framework", shell=True, check=True)
        print("msfvenom foi instalado com sucesso!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Erro ao instalar o msfvenom: {e}")
        return False

def check_veil_installed():
    try:
        subprocess.run("veil --version", shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

def install_veil():
    try:
        print("Iniciando a instalação do Veil-Framework...")
        subprocess.run("apt-get install -y git", shell=True, check=True)
        subprocess.run("git clone https://github.com/Veil-Framework/Veil.git", shell=True, check=True)
        subprocess.run("cd Veil && ./config/setup.sh --force --silent", shell=True, check=True)
        print("Veil-Framework foi instalado com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao instalar o Veil-Framework: {e}")

# Defina outras funções necessárias aqui, como create_listener, generate_payload, etc.

def main():
    print("Bem-vindo ao gerador de payloads usando msfvenom!")

    if not check_msfvenom_installed():
        if not install_msfvenom():
            print("Não foi possível instalar o msfvenom. O programa será encerrado.")
            return

    while True:
        print("\nMENU INICIAL:")
        print("1. Abrir Listener")
        print("2. Criar Exploits e Payloads")
        print("3. Instalar Veil-Framework")
        print("4. Atualizar Ferramentas")
        print("0. Sair")

        choice = input("Digite o número da opção desejada: ")

        if choice == "1":
            create_listener()
        elif choice == "2":
            # Implemente a lógica para criar payloads e exploits aqui.
            pass
        elif choice == "3":
            if not check_veil_installed():
                install_veil()
            else:
                print("O Veil-Framework já está instalado.")
        elif choice == "4":
            # Implemente a lógica para atualizar ferramentas aqui.
            pass
        elif choice == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")
            continue

if __name__ == "__main__":
    main()