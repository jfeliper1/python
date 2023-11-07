import math
altura = float(input('Indique sua altura: '))
peso = float(input('Indique seu peso: '))
imc = peso / (altura**2) *10000
print(f'Seu IMC é de: {imc}')
print('Confira o grau de gravidade de seu IMC.\n \n ABAIXO DE 17: MUITO ABAIXO DO PESO.\n \n ENTRE 17 E 18.50: ABAIXO DO PESO.\n \n ENTRE 18.50 E 24.99: PESO NORMAL.\n \n ENTRE 25 E 29.99: ACIMA DO PESO.\n \n ENTRE 30 E 40: OBESIDADE.')
