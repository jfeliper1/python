# 5. Ler dois números decimais a apresente na tela:
# - Soma dos dois números
# - Subtração dos dois números
# - Multiplicação dos dois números
# - Divisão dos dois números
# - Potência do primeiro elevado pelo segundo
# - Módulo (resto da divisão) entre os dois números [%]
# - Raiz quadrada dos dois números [math.sqrt()]

import math

num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
potencia = num1 ** num2
modulo = num1 % num2
raiz_q_num1 = math.sqrt(num1)
raiz_q_num2 = math.sqrt(num2)

print(f'Os números digitados foram: {num1} e {num2}')
print(f'O Resultado da soma dos números foi: {soma}')
print(f'O Resultado da Subtração foi: {subtracao}')
print(f'O Resultado da multiplicação foi: {multiplicacao}')
print(f'Dividindo os números chegamos a: {divisao}')
print(f'O Resultado da potencia foi: {potencia}')
print(f'A sobra (módulo) da divisão foi: {modulo}')
print(f'A raíz quadrada do númer {num1} número é: {raiz_q_num1}')
print(f'A raíz quadrada do númer {num2} número é: {raiz_q_num2}')




