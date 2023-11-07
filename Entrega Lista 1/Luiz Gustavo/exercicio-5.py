#Limpando o terminal
from os import system
q = system("cls")

#Importando a biblioteca math 
import math

#Exibindo mensagem na tela
print("Vamos efetuar cálculos matemáticos ? Para isso, você deve escolher dois números.")

#Pulando uma linha 
print ()

#Solicitando dois valores e convertendo os dados para números decimais
n1 = float(input("Digite um valor para n1:"))
n2 = float(input("Digite um valor para n2:"))

#Pulando uma linha 
print ()

#Somando os dois valores 
soma = (n1 + n2)

#Subtraindo os dois valores
subtracao = (n1 - n2)

#Multiplicando os dois valores
multiplicacao = (n1 * n2)

#Dividindo os dois valores
divisao = (n1 / n2)

#Calculando a potência do n1 pelo n2 
potencia = (n1 ** n2)

#Calculando o módulo do n1 pelo n2 
modulo = (n1 % n2)

#Calculando a raiz quadrada dos dois números 
raiz_n1 = math.sqrt(n1)
raiz_n2 = math.sqrt(n2)

#Exibindo todos os valores na tela 
print (f"A soma de {n1} e {n2} é {soma}")
print (f"A subtração de {n1} e {n2} é {subtracao}")
print (f"A multiplicação de {n1} e {n2} é {multiplicacao}")
print (f"A divisão de {n1} e {n2} é {divisao}")
print (f"A potência de {n1} elevado a {n2} é {potencia}")
print (f"A raiz quadrada de {n1} é {raiz_n1} e a raiz quadrada de {n2} é {raiz_n2}")
print (f"O resto da divisão entre {n1} e {n2} é {modulo}")

