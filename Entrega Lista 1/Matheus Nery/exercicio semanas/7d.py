from os import system
system('cls') or system('clear')

n = int(input('Informe o dia da semana [1...7]:'))

if n > 0:
    if n < 0:
        if n ==1:
            print('segunda')
        else:
            if n == 2:
                print('Terça')
            else:
                if n == 3:
                    print('Quarta')
                else:
                    if n == 4:
                        print('Quinta')
                    else:
                        if == 5:
                            print('Sexta')
                        else:
                            if n == 6:
                                print('sábado')
                            else:
                                if n == 7:
                                    print('Domingo')