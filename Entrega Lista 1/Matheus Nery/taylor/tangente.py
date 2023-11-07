from os import system
import sys
sys.path.insert(1, './modulo')
from modulo.seno import seno as s
from modulo.cosseno import cosseno as cos


def tangente(angulo):
    if angulo == 90:
        return'Não existe'
    return s(angulo) / cos(angulo)


if __name__ == '__main__':
    system('cls')
    ang = float(input('Informe o ângulo:  '))
    print(f'Tangente do {ang}: {tangente(ang)}\n')



    

