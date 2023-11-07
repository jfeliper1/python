import math, sys

continuar = True

while continuar:
    n=int(input('Digite um inteiro: '))
    print(f'Raiz quadrada de {n}={math.sqrt(n)}')
    op = input('\nContinuar? [S\n]: ').lower()[0]
    if op != 's':
        sys.exit()
