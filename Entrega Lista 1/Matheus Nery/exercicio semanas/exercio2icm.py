'''Crie um programa em Python que a partir do peso e altura de uma pessoa, calcule e informe 
o IMC (Índice de massa corpóreo) arredondado, informando também o estado da pessoa 
baseado na tabela abaixo.'''

from os import system

system('cls') or system('clear')

peso = float(input('Informe seu peso:'))
altura = float(input('Informe sua altura:'))

imc = peso / altura ** 2

print(f'Seu imc atual é {round (imc, 1)}')

if imc < 17:
    print('Você está muito abaixo do peso')
elif 17 <= imc < 18.5:
    print('Abaixo do peso')
elif 18.5 >= imc < 25:
    print('Peso Normal')
elif 25 <= imc < 30:
    print('Obesidade 1')
elif 35 <= imc < 40:
    print('Obesidade 2 (Severa)')
else:
    print('Obesidade 3 (mórbida)')
