#Limpando o terminal
from os import system
q = system("cls")

#Importando a biblioteca math
import math

#Exibindo mensagem
print("Vamos calcular o perímetro de uma circunferência ?\nPara isso, informe o valor do raio da Circunferência.")

#pulando uma linha 
print()

#Solicitando o valor do raio da circunferência e convertendo o dado para número decimal
raio = float(input("Digite o valor do raio da circunferência:"))

#Calculando o perímetro da circunferência 
perimetro_circ = (2 * math.pi * raio)

#pulando uma linha 
print()

#Exibindo o valor do perimetro arredondado com duas casa decimais 
print(f"O valor do perímetro da circunferência é: {round(perimetro_circ,2)}")
