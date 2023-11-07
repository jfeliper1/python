
# 4. Crie um programa em Python que calcule a área de uma circunferência e exiba o valor 
# arredondado com duas casas decimais.
import math
raio = float(input("Informe um raio: "))
area_circ = math.pi * raio ** 2
print(f"A área de uma circunferência é : {round(area_circ, 2)}")