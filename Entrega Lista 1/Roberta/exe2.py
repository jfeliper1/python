"""2. Crie um programa em Python que solicite o valor da base e altura e calcule a área de um 
triângulo, apresentando no final todos os valores na tela.
area_triangulo = base x altura / 2
"""


base = float(input('\nDigite o valor da base: \n'))
altura = float(input('\nDigite o valor da altura: \n'))

area = (base * altura) / 2

print(f'\nA area do triângulo de acordo com a BASE: {base}cm e a ALTURA: {altura}cm é:/n {area}cm\n')