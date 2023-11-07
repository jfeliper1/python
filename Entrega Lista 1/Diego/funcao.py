from os import system
system ('cls')

def barra(texto):
    for i in range(len(texto)+2):
        print(f'{ch}', end='')
    print()

###################################################

frase = input('\nDigite uma frase: ')
barra(frase)
ch = '\u2588'
print(f"{ch}{frase}{ch}")

