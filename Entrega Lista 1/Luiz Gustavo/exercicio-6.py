#Limpando o terminal
from os import system
q = system("cls")

#Exibindo mensagem na tela 
print(f"Quer saber quantos reais de desconto vai receber naquele produto ? \nDeixe-me ajudá-lo.\nPara isso, informe o valor do produto desejado e também a porcentagem de desconto que será recebida.")

#Pulando uma linha
print()

#Solicitando o valor do produto e convertendo o dado para número decimal
valor_produto = float(input("Digite o valor do produto:"))

#Solicitando a porcentagem de desconto e convertendo o dado para número decimal
porcentagem_desc = float(input("Digite a porcentagem de desconto deste produto:"))

#Calculando o valor do desconto
valor_desconto = (valor_produto * porcentagem_desc / 100)

#Calculando o valor final do produto
valor_final = (valor_produto - valor_desconto)

#Pulando uma linha
print()

#Exibindo o valor final do produto na tela
print(f"Um produto que custa R${valor_produto} com {porcentagem_desc}% de desconto aplicado, custará no final: R${valor_final}")
