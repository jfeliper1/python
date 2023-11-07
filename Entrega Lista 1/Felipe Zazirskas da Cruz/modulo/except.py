from os import system 
system('cls')

try :
    n1 = float(input('Informe o 1º Nº : '))
    n2 = float(input('Informe o 2º Nº : '))
    print(f'\n\n{n1} / {n2} = {n1 / n2}\n\n')

except ValueError:
    print('\n\nVocê deve digitar apenas numeros inteiros\n\n ')

except ZeroDivisionError:
    print('\n\nO Segundo valor não pode ser zero\n\n')

except :
    print('\n\nErro inesperado\n\n')