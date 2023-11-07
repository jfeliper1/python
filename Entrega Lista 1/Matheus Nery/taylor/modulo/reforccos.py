
from os import system
from fatorial import fatorial 
from radiano import radiano 

def cosseno(angulo):
    x = radiano(angulo)
    cos = 1
    ref = True

    for i in range(2, 160+2, 2):
        if ref:
            cos -= x**i / fatorial(i)  #cos = cos - x**i / fat(i)
        else:
            cos += x**i / fatorial(i)     
            ref = True
    return round(cos, 4) 

if __name__ == '__main__':
    system('cls')
    ang = float(input('Informe a medida do ângulo:  '))
    print(f'O cosseno de {ang}: é igual a {cosseno(ang)} ')




            