from os import system
import math

def radiano(angulo):
    return angulo * math.pi / 180

if __name__ == '__main__':
    system('cls')
    ang = float(input(f'\nInforme a medida do ângulo: [0º ... 360º]: '))
    print(f'\n{ang}º equivale a {radiano(ang)} radianos')

