from os import system


def barra(texto): #quando você chama se torna parametro
    ch = '\u2588'
    for i in range(len(texto)+4):
        print(f'{ch}', end='')
    print()

if __name__ == '__main__':
    system('cls')
    frase = input('\nDigite uma frase:\n')
    ch = '\u2588'
    barra(frase)
    barra(frase)
    print(f'{ch} {frase} {ch}')
    barra(frase)
    barra(frase)