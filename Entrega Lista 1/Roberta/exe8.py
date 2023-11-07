"""
8. Crie um programa em Python para converter e exibir uma temperatura de graus Celsius para 
graus Fahrenheit.

F =        9 * C + 150
            -----------
                5
"""

celsius = int(input('/nQuantos graus está ? \n'))
fahrenheit = (9 * celsius + 150) / 5

print(f'\nO grau celsius convertido para fahrenheit é: {fahrenheit}')