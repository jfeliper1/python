from os import system 

def barra(texto):
    ch = '\u2588'
    for i in range(len(texto)+2):
        print(f'{ch}', end='')
    print()

    
if __name__=='__main__':
    system ('cls')
    frase = input('\nDigite uma frase:\n')
    barra(frase)
    barra(frase)
    ch = '\u2588'
    print(f"{ch}{frase}{ch}")
    barra(frase)
    barra(frase)