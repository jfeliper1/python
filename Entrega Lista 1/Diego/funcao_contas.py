from os import system
import math


def menu():
    system('cls')
    print('**CALCULADORA INTELIGENTE**')
    print('1. SOMA')
    print('2. SUBTRAÇÃO')
    print('3. MULTIPLICAÇÃO')
    print('4. DIVISÃO')
    op = int(input('\nOpção: '))
    return op
    


def entrada():
    n1= float(input('\nDigite o 1° n°: '))
    n2= float(input('\nDigite o 2° n°: '))






# Função para somar
def somar (n1,n2):
    soma = n1+n2


# Função para subtrair
def subtrair(n1,n2):
    sub = n1-n2


# Função para multiplicar
def multiplicar(n1,n2):
    mult = n1*n2


# Função para dividir
def dividir(n1,n2):
    div = n1/n2


if __name__=='__main__':
    op = menu()
num1,num2 = entrada()

match op:
    case 1:
        somar(n1+n2)
        print('O resultado é:', num1+num2)
    case 2:
        subtrair(n1-n2)
        print('O resultado é:', num1-num2)
    case 3:
        multiplicar(n1*n1)
        print('O resulado é:', num1*num2)
    case 4:
        dividir(n1/n2)
        print('O resultado é:', num1/num2)
    case _:
        menu()