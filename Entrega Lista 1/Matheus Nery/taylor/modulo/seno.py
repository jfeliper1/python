from os import system
#import fatorial as fat
#import fatorial import fatorial 
#import fatorial
#formas de importar o nossa bibliotecas.
from fatorial import fatorial
import radiano

def seno(angulo):
    x = radiano.radiano(angulo)
    sin = x 
    ref = True
    for i in range(3, 160+2, 2):
        if ref:
            sin -= x ** i / fatorial(i)
            ref = False
        else:
            sin += x ** i / fatorial(i)
            ref = True
    return round(sin, 4)


if __name__ == '__main__':
    system('cls')
    graus = float(input(f'\nInforme a medida do ângulo:  '))
    print(f'\nO seno de {graus}º : {seno(graus)}')
    







