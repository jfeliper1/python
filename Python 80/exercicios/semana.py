from os import system
system('cls')

num = int(input('Insira o número do dia correspondente:'))

if 1 <= num <=7 :
    if num == 1:
        print(f'Dia correspondente a segunda feira')
    elif num == 2 :
        print(f'Dia correspondente a terça feira')
    elif num == 3 :
        print(f'Dia correspondente a quarta feira')
    elif num == 4 :
        print(f'Dia correspondente a quinta feira')
    elif num == 5 :
        print(f'Dia correspondente a sexta feira')
    elif num == 6 :
        print(f'Dia correspondente a sábado')
    elif num == 7 :
        print(f'Dia correspondente a Domingo')
else :
    print('Número inválido !')
     

        