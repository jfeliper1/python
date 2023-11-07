# 7. Crie um programa em Python que faça a conversão de um valor em Dólar [USA] para o seu 
# equivalente em Real. Deve ser informada a taxa de câmbio e o valor em dólar para a conversão
from os import system
system ('cls')

valor= float(input("digite a quantia a ser convertida: U$"))

dolarhoje= float(input("O valor de 1 dolar hoje é: "))

valor_convertido= valor * dolarhoje

print (f'Seu capital a ser convertido é: ${valor}')
print (f'Portanto, você receberá : R${valor_convertido}')