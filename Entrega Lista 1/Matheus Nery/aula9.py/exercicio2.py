import math
from os import system
system('cls')

numero = float(input('Informe um número?')) # <--- float foi utilizado, pois fiz o código para receber número decimais.

if numero % 2 == 0: # <-- O número informado dividido por 2, porém utilizamos o módulo para verificar se há resto da divisão e informar o usuário, se não houver é par, se hover é ímpar.
    print(f'O {numero} é par')
else:
    print(f'O {numero} é impar')

