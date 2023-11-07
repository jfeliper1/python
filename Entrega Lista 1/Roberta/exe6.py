"""
6. Crie um programa em Python para calcular o valor final de uma compra, com desconto 
percentual qualquer.
"""

compra = float(input('\nQual valor do produto: \n'))
desconto = float(input('\nQual valor do desconto: \n'))

desconto_total = (desconto / compra) * 100


print(f'\nA area do retangulo de acordo com a BASE: {compra}cm e a ALTURA: {desconto}cm é: {desconto_total}cm\n')