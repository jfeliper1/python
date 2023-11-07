# Crie um programa em Python que solicite que o usuário informe um número entre 1 e 7 e 
# exiba na tela:
# Segunda-feira caso o número digitado seja 1
# Terça-feira-feira caso o número digitado seja 2
# ...
# Sábado caso o número digitado seja 6
# Domingo caso o número digitado seja 7
# Obs.: Caso o número que o usuário informou esteja fora do limite estabelecido deve ser 
# exibida uma mensagem na tela indicando que o número é inválido


from sqlalchemy import case
from traitlets import default

from os import system

system("cls")

def case1():
    print("Segunda")

def case2():
    print("Terça")

def case3():
    print("Quarta")

def case4():
    print("Quinta")

def case5():
    print("Sexta")

def case6():
    print("Sábado")

def case7():
    print("Domingo")

# Mapeia valores aos casos
casos = {
    1: case1,
    2: case2,
    3: case3,
    4: case4,
    5: case5,
    6: case6,
    7: case7,
}

# Valor de entrada
dia = int(input("Digite um número entre 1 e 7: "))

# Executa a ação associada ao valor
if dia in casos:
    casos[dia]()
else:
    print("Valor não corresponde a nenhum caso")
