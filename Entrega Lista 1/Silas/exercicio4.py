#4.   Crie um programa em Python que calcule a área de uma circunferência e exiba o valor 
#arredondado com duas casas decimais.
#area_circ = π * raio²

import math

raio= float(input("digite o valor do raio: "))

area= math.pi * raio**2

print (f'O valor do raio da sua circunferencia é: {raio}')
print (f'Portanto, o valor do area da sua circunferência é: {round(area,2)}')