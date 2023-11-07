# Crie um programa em Python que calcule a área de uma circunferência e exiba o valor 
# arredondado com duas casas decimais.
# area_circ = π * raio²


import math

raio = float(input("Digite o valor do raio: "))

area_circ = math.pi * math.pow(raio, 2)

print(f'O valor do raio é de: {raio} metros.\nSendo assim, a área da circunferência é de: {round(area_circ,2)} metros.\n')


