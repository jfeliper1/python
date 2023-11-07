#Limpando o terminal
from os import system
q = system("cls")

#Exibindo mensagem
print("Vamos calcular a área de um retângulo ?\nPara isso, informe o valor da base e da altura do retângulo.")

#pulando uma linha 
print()

#Solicitando valor da base do retângulo e convertendo o dado para numero inteiro 
base = int(input("Digite o valor da base do retângulo:"))

#Solicitando valor da altura do retângulo e convertendo o dado para numero inteiro
altura = int(input("Digite o valor da altura do retângulo:"))

#Calculando a área do retângulo
area_retangulo = (base*altura)

#pulando uma linha 
print()

#Exibindo os valores da base, altura e área do retângulo
print(f"Um retângulo de base:{base} e altura:{altura} tem uma área de:{area_retangulo}")
