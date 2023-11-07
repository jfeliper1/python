"""
5. Ler dois números decimais a apresente na tela:
- Soma dos dois números
- Subtração dos dois números
- Multiplicação dos dois números
- Divisão dos dois números
- Potência do primeiro elevado pelo segundo
- Módulo (resto da divisão) entre os dois números [%]
- Raiz quadrada dos dois números [math.sqrt()]
"""

import math

num1 = float(input('\nDigite o primeiro número: \n'))
num2 = float(input('\nDigite o segundo número: \n'))

adi = num1 + num2
sub = num1 - num2
mult = num1 * num2
div = num1 / num2
pot = num1 ** num2
mod = num1 % num2
raiz1 = math.sqrt(num1)
raiz2 = math.sqrt(num2)

print(f'\n RESULTADO: \n\n ADIÇÃO: {adi} \n SUBTRAÇÃO: {sub}\n MULTIPLICAÇÃO: {mult}\n DIVISÃO: {pot}\n POTÊNCIA: {pot}\n MÓDULO: {mod}\n RAIZ QUADRADA DO NÚMERO 1: {round(raiz1,2)}\n RAIZ QUADRADA DO NÚMERO 2: {round(raiz2,2)}\n')