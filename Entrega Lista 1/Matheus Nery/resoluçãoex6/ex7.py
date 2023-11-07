from os import system
import sys

system('cls')

while True:
    n = int(input('\nDigite um nº >= 2: '))
    if n >= 2:
        break

for i in range(2, n//2+1):
    if n % i == 0:
        print(f'\n{n} não é primo, pois é divisível por {i}.')
        sys.exit()
print(f'{n} o número é primo')
