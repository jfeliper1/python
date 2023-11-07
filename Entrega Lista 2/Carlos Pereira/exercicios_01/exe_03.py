

# 3. Crie um programa em Python que calcule o perímetro de uma circunferência e exiba o valor 
# arredondado com duas casas decimais.
# perimetro_circ = 2 * π * raio


# r= 2π C

import math

print("\nCALCULADORA DO PERÍMETRO DA CIRCUNFERÊNCIA")
raio = float(input("Digite o valor do raio do círculo:  "))

perimetro = 2 * math.pi * raio

print("****************** RESULTADO ****************************")
print(f"O perímetro da circunferência com raio {raio} é: {round(perimetro, 2)}")
print("*********************************************************")

