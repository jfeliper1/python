
# 1 - área do retângulo
# base = float(input("Digite a base:"))
# altura = float(input("Digite a altura:"))
# area_retangulo = base * altura
# print(f"A área do retângulo é: {area_retangulo}")

# # 2 - área triângulo
# base = float(input("Digite a base: "))
# altura = float(input("Digite a altura: "))
# area_triangulo = (base * altura) / 2

# 3 - Crie um programa em Python que calcule o perímetro de uma circunferência e exiba o valor 
# arredondado com duas casas decimais.
import math
raio = float(input("Informe um raio: "))

perimetro = 2 * math.pi  * raio
print(f"o perímetro de uma circunferência é : {round(perimetro, 2)}")
