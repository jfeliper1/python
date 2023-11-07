from os import system
system('cls') or system('clear')

n = int(input('Informe o dia da semana [1...7]:'))

if n < 0:
    if n > 7:
        if n == 1:
            print('segunda')
         elif n == 2:
             print('Terça')
         elif n == 3:
             print('Quarta')
         elif n == 4:
             print('Quinta')
         elif n == 5:
             print('Sexta')
         elif n == 6:
             print('sábado')
         elif n == 7:
             print('Domingo')
    else:
        print('Dia inválido')
else:
    print('Dia inválido')