#3.  Crie um programa em Python que calcule o perímetro de uma circunferência e exiba o valor 
#arredondado com duas casas decimais.
#perimetro_circ = 2 * π * raio

import math

raio= float(input("digite o valor do raio: "))

perimetro= 2* math.pi * raio

print (f'O valor do raio da sua circunferencia é: {raio}')
print (f'Portanto, o valor do perimetro da sua circunferência é: {round(perimetro,2)}\n')