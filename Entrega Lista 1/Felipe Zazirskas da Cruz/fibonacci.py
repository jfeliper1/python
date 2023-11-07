from os import system
import sys

system('cls')

while True:
    qtde = int(input(f'Digite um nro >=0:  '))
    if qtde>= 0:
        break

if qtde==0:
    print('O Programa sera encerrado.\n\n')
    sys.exit()

if qtde==1:
    print(f'\n 1 \n')
    sys.exit()
    

n1 = n2 = 1

print(f'\n\n{n1}  {n2}', end ="  ")

for i in range(qtde -2):
    print(f'**{round(n1/n2, 4)}**', end='    ')
    n3 = n1 + n2
    print(f'{n3}',end="  ")
    n1 = n2
    n2 = n3

