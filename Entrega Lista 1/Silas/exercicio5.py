#5 - Ler dois números decimais a apresente na tela:
# - Soma dos dois números
# - Subtração dos dois números
# - Multiplicação dos dois números
# - Divisão dos dois números
# - Potência do primeiro elevado pelo segundo
# - Módulo (resto da divisão) entre os dois números [%]
# - Raiz quadrada dos dois números [math.sqrt()]


import math

n1= float(input("digite um numero: "))

n2= float(input("digite outro numero: "))

soma= n1+n2
subtra=n1-n2
multi=n1*n2
divisao=n1/n2
poten=n1**n2
modulo=n1%n2
raiz1=math.sqrt(n1)
raiz2= math.sqrt(n2)

print (f'Voce digitou o número: {n1}\n e voce digitou o número: {n2}')
print (f'A soma dos números que você escolheu é: {soma}')
print (f'A subtração dos números que você escolheu é: {subtra}')
print (f'A multiplicação dos números que você escolheu é: {multi}')
print (f'A divisão dos números que você escolheu é: {divisao}')
print (f'A Potência do primeiro número elevado pelo segundo número que você escolheu é: {poten}')
print (f'O modulo dos números que você escolheu é: {modulo}')
print (f'A raiz quadrada do 1°número que você escolheu é: {raiz1}')
print (f'A raiz quadrada do 2°número que você escolheu é: {raiz2}')