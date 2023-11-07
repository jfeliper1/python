'''Programa ímpar 2.0 programa utilizado para informar ao usuário se o número informado é par ou impar'''

from os import system
system('cls')

numero = int(input('Informe um número?')) # <--- int foi utilizado, pois fiz o código para receber número inteiros.

if numero >= 0:
   if numero % 2 == 0:
      print(f'{numero} é um número par')
   else:
      print(f'{numero} é impar')
else:
   print(f'{numero} é um valor invalido')

    