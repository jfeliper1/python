#Limpando o terminal
from os import system
q = system("cls")

#Exibindo mensagem na tela 
print("Vamos converter a temperatura atual em graus Celsius para a mesma temperatura em Fahrenheit ?\nPara isso, informe a temperatura em graus Celsius atual do ambiente onde você está agora.")

#Pulando uma linha 
print()

#Solicitando a temperatura atual e convertendo o dado para número decimal
temperatura_cel = float(input("Digite a temperatura em graus Celsius atual do ambiente em que se encontra:"))

#Convertendo a temperatura de graus Celsius para graus Fahrenheit.
temperatura_fah = (((9 * temperatura_cel) + 150) /5)

#Pulando uma linha 
print()

#Exibindo mensagem na tela 
print(f"A temperatura atual do ambiente: {temperatura_cel}, convertida para graus Fahrenheit é igual a: {temperatura_fah}")