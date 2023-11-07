from os import system
system('cls')

frase = input('\nDigite uma frase:\n')
ch = '\u2588'

for i in range(len(frase)+4):
    print(f'{ch}', end='')

print(f'{ch} {frase} {ch}')

for i in range(len(frase)+4):
    print(f'{ch}', end='')

for i in range(len(frase)+4):
    print(f'{ch}', end='')