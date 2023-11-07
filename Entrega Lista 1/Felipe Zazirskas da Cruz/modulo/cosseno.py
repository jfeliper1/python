from os import system
from fatorial import fatorial as fat
from radiano import radiano as rad


def cosseno(angulo):
    x = rad(angulo)
    cos = 1
    ref = True

    for i in range(2, 160+2, 2):
        if ref:
            cos -= x ** i/fat(i)
            ref = False
        else:
            cos += x ** i/fat(i)
            ref = True
    return round(cos, 4)


r = rad(90)
print(r)


f = fat(5)
print(f)


if __name__=='__main__':
    system('cls')
    graus = float(input(f'\nInforme a medida do angulo :' ))
    print(f'\n O cosseno de {graus}º equivale a {cosseno(graus)}\n\n')
                      