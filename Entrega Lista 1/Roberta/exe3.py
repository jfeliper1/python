"""3. Crie um programa em Python que calcule o perímetro de uma circunferência e exiba o valor 
arredondado com duas casas decimais.
perimetro_circ = 2 * π * raio
"""

base = float(input('\nDigite o valor da base: \n'))
altura = float(input('\nDigite o valor da altura: \n'))

perimetro = base / altura ** 2


print(f'\nA area do retangulo de acordo com a BASE: {base}cm e a ALTURA: {altura}cm é: {round(perimetro,2)}\n')

