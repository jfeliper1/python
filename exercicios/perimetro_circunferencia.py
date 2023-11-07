import math

raio = float(input("Digite o raio da circunferência: "))

perimetro = 2 * math.pi * raio

perimetro_arredondado = round(perimetro, 2)

print(f"O valor do perímetro da circunferência é {perimetro_arredondado}")