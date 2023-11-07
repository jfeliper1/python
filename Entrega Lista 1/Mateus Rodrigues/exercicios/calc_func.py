import math 

number1 = float(input('Digite o primeiro número decimal: '))
number2 = float(input('Digite o segundo número decimal: '))

#calc

sum = number1 + number2
subtraction = number1 - number2
multiplicaion = number1 * number2
division = number1 / number2
potencia = number1 ** number2
modulo = number1 % number2
raiz1 = math.sqrt(number1)
raiz2 = math.sqrt(number2)

# results

print(f'O resultado da soma é: {sum}')
print(f'O resultado da subtração é: {subtraction}')
print(f'O resultado da multiplicação é: {multiplicaion}')
print(f'O resultado da divisão é: {division}')
print(f'O resultado da potencia é: {potencia}')
print(f'O resultado do modulo é: {modulo}')
print(f'O resultado da raiz quadrada do primeiro número é: {raiz1}')
print(f'O resultado da raiz quadrada do segundo número é: {raiz2}')