""". Crie um programa em Python que faça a conversão de um valor em Dólar [USA] para o seu 
equivalente em Real. Deve ser informada a taxa de câmbio e o valor em dólar para a 
conversão.
"""


dolar = float(input('\nQuanto dinheiro você tem em dolar: \n'))
cambio = float(input('\nQuanto custa 1 dolar em real: \n'))

real = dolar * cambio

print(f'\nVocê tem {dolar} em dolares e a taxa de cambio {cambio}. Sendo assim, você tem R$ {real}')