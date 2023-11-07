# Crie um programa em Python que calcule o perímetro de uma circunferência e exiba o valor 
# arredondado com duas casas decimais.
# perimetro_circ = 2 * π * raio

import math

raio = float(input("Digite o valor do raio: "))

perimetro_circ = 2 * math.pi * raio

print(f'se o raio tem: {raio} metros\n o perímetro da circunferência é de: {round(perimetro_circ,2)}\n')


