from os import system
from seno import seno as s
from cosseno import cosseno as c


def tangente(angulo):
    if angulo == 90:
        return 'Não exite'
    return s(angulo)/c(angulo)


if __name__=='__main__':
    system('cls')
    ang = float(input(f'\nInforme a medida do angulo :' ))
    print(f'\n A Tangente de {ang}º equivale a {tangente(ang)}\n\n')
                      