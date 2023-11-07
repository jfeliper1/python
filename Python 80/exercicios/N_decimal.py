import math


numero1 = float(input("Digite o primeiro número decimal: "))
numero2 = float(input("Digite o segundo número decimal: "))


soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2
potencia = numero1 ** numero2
modulo = numero1 % numero2
raiz_quadrada1 = math.sqrt(numero1)
raiz_quadrada2 = math.sqrt(numero2)

print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
print(f"Potência: {potencia}")
print(f"Módulo: {modulo}")
print(f"Raiz quadrada do primeiro número: {raiz_quadrada1}")
print(f"Raiz quadrada do segundo número: {raiz_quadrada2}")