from click import clear
clear()
frase = input('Digite uma frase: ')
ch = '\u2588'
for i in range(0, len (frase)+2):
    print(ch, end='')
print(f'\n{ch} {frase} {ch}')
