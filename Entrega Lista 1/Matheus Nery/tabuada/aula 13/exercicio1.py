from os import system
system('cls') or system('clear')

frase = input('\nDigite uma frase: ')
ch = '\u2588'

for i in range(len(frase)+2):
    print(f'{ch}', end='')

print(f'\n{ch}{frase}{ch}')

for i in range(len(frase)+2):
    print(f'{ch}', end='')
