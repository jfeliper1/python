from os import system
system('cls')

# contador
tentativa = 0

# user
login = 'user'
password = '12345'

while tentativa < 3 :
    login = input('Insira sua identificação de login:')
    password = input('Insira a senha:')

    if login == 'user' and password == '12345' :
        print('Acesso permitido')
        break
    else :
        print('Acesso negado, tente novamente')
        tentativa += 1 

if tentativa == 3:
    print('Limite de tentativas atingido')


    