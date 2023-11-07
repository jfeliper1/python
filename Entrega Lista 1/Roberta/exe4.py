"""
4. Crie um programa em Python que calcule a área de uma circunferência e exiba o valor 
arredondado com duas casas decimais.
area_circ = π * raio²
"""

import math

base = float(input('\nDigite o valor da base: \n'))
altura = float(input('\nDigite o valor da altura: \n'))

circ = base / (math.pow(altura,2))


print(f'\nA area do retangulo de acordo com a BASE: {base}cm e a ALTURA: {altura}cm é: {round(circ,2)}\n')
