from os import system
system('cls') or system('clear')

import math, sys


while True:
    n = int(input('Digite um número inteiro: '))
    print(f'Raiz quadrada de {n} = {math.sqrt(n)}')
    op = input('\nDeseja continuar? [S/N]: ').lower()[0]
    if op != "s" :
        sys.exit()

        





