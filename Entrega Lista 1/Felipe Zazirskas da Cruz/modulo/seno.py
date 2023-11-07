from os import system
from fatorial import fatorial
from radiano import radiano


def seno(angulo):
    x = radiano(angulo)
    sen = x
    ref = True

    for i in range(3, 160+2, 2):
        if ref:
            sen -= x ** i/fatorial(i)
            ref = False
        else:
            sen += x ** i/fatorial(i)
            ref = True
    return round(sen, 4)


r = radiano(90)
print(r)


f = fatorial(5)
print(f)


if __name__=='__main__':
    system('cls')
    graus = float(input(f'\nInforme a medida do angulo :' ))
    print(f'\no Seno de {graus}º equivale a {seno(graus)}\n\n')
                      