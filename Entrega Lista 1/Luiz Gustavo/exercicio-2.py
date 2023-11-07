#Limpando o terminal
from os import system
q = system("cls")

#Exibindo mensagem
print("Vamos calcular a área de um triângulo ?\nPara isso, informe o valor da base e da altura do triângulo.")

#pulando uma linha 
print()

#Solicitando o valor da base do triângulo e convertendo o dado para número inteiro 
base = int(input("Digite o valor da base do triângulo:"))

#Solicitando o valor da altura do triângulo e convertendo o dado para número inteiro 
altura = int(input("Digite o valor da altura do triângulo:"))

#Calculando a área do triângulo
area_triangulo = (base * altura / 2) 

#pulando uma linha 
print()

#Exibindo os valores da base, altura e area do triângulo 
print(f"Um trinângulo de base:{base} e altura:{altura} tem uma área de:{area_triangulo}")