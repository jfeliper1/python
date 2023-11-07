from os import system
import getpass

system('cls')

user_card= 'Felipe'
senha_card= 'senha123'

for i in range(3):
    user = input('\n\n\t\tDigite seu usuário:')
    senha = getpass.getpass('\n\n\t\tSenha:')

    if user == user_card and senha== senha_card:
        system('cls')
        print(f'\n\n\t\tSeja bem vindo Sr(a) {user}.\n')
        break
    print(f'\n\n\t\t **DADOS INCORRETOS**')
    print(f'\n\n\t\t Faltam {2-i} tentativas.')
                  

