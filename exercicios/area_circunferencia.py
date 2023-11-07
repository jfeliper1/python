import math


raio = float(input("Digite o raio do círculo: "))

area = math.pi * (raio ** 2)

area_arredondada = round(area, 2)

print(f"A área do círculo é {area_arredondada}")