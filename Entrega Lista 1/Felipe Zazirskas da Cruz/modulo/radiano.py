from os import system
import math

def radiano(angulo):
    return angulo * math.pi / 180


if __name__=='__main__':
    system('cls')
    ang =float(input(f'Informe a medida do angulo [0...360º]: '))
    print(f'\n{ang}º é equivalente a {radiano(ang)} radianos \n\n')

