from os import system

system('clear')

n = int(input('Informe um nº inteiro: '))

for i in range(0, 101):
    print(f'{n} x {i} = {n * i}')



