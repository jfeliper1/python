from os import system   
import sys
system('cls')

try:
    n1 = int(input('Informe o 1º número da operação: '))
    n2 = int(input('Informe o 2º número da operação: '))
    print(f' {n1} / {n2} = {n1} / {n2}')
except ValueError:
    print('Digite um número inteiro')
except ZeroDivisionError:
    print('Digite um número inteiro e diferente de 0')
except SyntaxError:
    print('Erro do programador')
except:
    print('Erro inesperado')

sys(exit)
