import time
import os

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("Bem-vindo ao programa de registro de nomes!")
    print("Escolha uma opção:")
    print("1. Registrar nome com validação simples")
    print("2. Registrar nome com validação avançada")

    # Captura erros caso o usuário digite um valor inválido
    try:
        escolha = int(input("Escolha uma opção (1 ou 2): "))
        if escolha not in [1, 2]:
            raise ValueError
    except ValueError:
        print("Opção inválida! Por favor, escolha 1 ou 2.")
        time.sleep(2)
        continue

    # Função para validação simples com contador regressivo
    def op1():
        while True:
            entrada = input("Digite seu nome: ").strip()
            if  entrada.replace(" ","").isalpha():
                os.system("cls" if os.name == "nt" else "clear")
                print(f"Olá, {entrada.title()}! \nSeu nome foi registrado com sucesso.")
                time.sleep(2)
                exit()
            else:
                print("Nome inválido! Por favor, digite apenas letras.")
                time.sleep(3)
                
                # Contador regressivo antes de permitir nova tentativa
                for segundos in range(3, 0, -1):
                    os.system("cls" if os.name == "nt" else "clear")
                    print(f"Tentando novamente em {segundos} segundos...")
                    time.sleep(1)
                os.system("cls" if os.name == "nt" else "clear")

    # Função para validação avançada com contador regressivo
    def op2():
        while True:
            try:
                nome = input("Digite seu nome: ").strip()
                if not nome.replace(" ", "").isalpha():  # Permite nomes compostos
                    os.system("cls" if os.name == "nt" else "clear")
                    raise ValueError("O nome deve conter apenas letras e espaços.")
                
                print(f"Olá, {nome.title()}! \nSeu nome foi registrado com sucesso.")
                time.sleep(4)
                exit()
                
            except ValueError as e:
                print(f"Erro: {e}. Tente novamente.")
                time.sleep(2)

                # Contador regressivo antes de permitir nova tentativa
                for segundos in range(5, 0,-1):
                    os.system("cls" if os.name == "nt" else "clear")
                    print(f"Tentando novamente em {segundos} segundos...")
                    time.sleep(1)
                os.system("cls" if os.name == "nt" else "clear")

    # Chama a função correta dentro do loop principal
    if escolha == 1:
        op1()
    elif escolha == 2:
        op2()