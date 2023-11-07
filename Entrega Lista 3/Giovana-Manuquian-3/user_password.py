from os import system

system('cls')

user = "Giovana"
password = 123
attempts = 3

for attempt in range(attempts):
    username_input = input("Digite seu usuário: ")
    password_input = input("Digite sua senha: ")

    if user == username_input and password == int(password_input):
        print("Acesso Permitido. Bem-vindo, Giovana!")
        break
    else:
        remaining_attempts = attempts - (attempt + 1)
        if remaining_attempts > 0:
            print(f"Acesso negado. Você tem {remaining_attempts} tentativas restantes.")
        else:
            print("Acesso negado. Todas as tentativas esgotadas. O sistema será bloqueado.")
