from os import system
system('cls')


def fatorial(numero):
    fat = 1
    for i in range (numero, 1, -1):
        fat *= i
    return fat


if __name__=='__main__':
    system('cls')
    print()

    while True:
        n = int(input(f'\n\t\t Digite um nº inteiro >=0:  '))
        if n >=0:
            break
   
    print(f'\n\t\t\t\t\t{n}!={fatorial(n)}\n')





