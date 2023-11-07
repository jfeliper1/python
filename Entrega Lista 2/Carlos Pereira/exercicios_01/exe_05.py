# Ler dois números decimais a apresente na tela:
# - Soma dos dois números
# - Subtração dos dois números
# - Multiplicação dos dois números
# - Divisão dos dois números
# - Potência do primeiro elevado pelo segundo
# - Módulo (resto da divisão) entre os dois números [%]
# - Raiz quadrada dos dois números [math.sqrt()]

import math
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

soma = n1 + n2
sub = n1 - n2
mul = n1 * n2
div = n1 / n2
pot = n1 ** n2
mod = n1 % n2
raiz1 = math.sqrt(n1)
raiz2 = math.sqrt(n2)

print("Soma:", soma)
print("Subtração:", sub)
print("Multiplicação:", mul)
print("Divisão:", div)
print("Potência:", pot)
print("Módulo:", mod)
print("Raiz quadrada do primeiro número:", raiz1)
print("Raiz quadrada do segundo número:", raiz2)
