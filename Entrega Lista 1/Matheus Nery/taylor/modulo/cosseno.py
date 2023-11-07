from os import system
#import fatorial as fat
#import fatorial import fatorial 
#import fatorial
#formas de importar o nossa bibliotecas.
from fatorial import fatorial
import radiano

def cosseno(angulo):
    x = radiano.radiano(angulo)
    cos = x
    ref = True
    for i in range(2, 160+2, 2):
        if ref:
            cos -= x ** i / fatorial(i)
            ref = False
        else:
            cos += x ** i / fatorial(i)
            ref = True
    return round(cos, 4)


if __name__ == '__main__':
    system('cls')
    graus = float(input(f'\nInforme a medida do ângulo:  '))
    print(f'\nO coseno de {graus}º : {cosseno(graus)}')
    







