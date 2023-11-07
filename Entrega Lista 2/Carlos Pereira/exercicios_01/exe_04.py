import math
# . Crie um programa em Python que calcule a área de uma circunferência e exiba o valor 
# arredondado com duas casas decimais.
# area_circ = π * raio²


import math

print("\nCALCULADORA DA ÁREA DA CIRCUNFERÊNCIA")
raio = float(input("Digite o valor do raio do círculo:  "))

area = math.pi * math.pow(raio, 2)

print("****************** RESULTADO ****************************")
print(f"A área da circunferência com raio {raio:.2f} é de: {round(area, 2)}")
print("*********************************************************")
