#Limpando o terminal
from os import system
q = system("cls")

#importando a biblioteca math
import math

#Exibindo mensagem
print("Vamos calcular a área de uma circunferência ?\nPara isso, informe o valor do raio da Circunferência.")

#pulando uma linha 
print()

#Solicitando o valor do raio da circunferência e convertendo o dado para número decimal 
raio = float(input("Digite o valor do raio da circunferência:"))

#Calculando o valor da área da circunferência 
area_circ = (math.pi * raio ** 2)

#pulando uma linha 
print()

#Exibindo o valor da área da circunferência com duas casas decimais 
print(f"O valor da área da circunferência é: {round(area_circ,2)}")



