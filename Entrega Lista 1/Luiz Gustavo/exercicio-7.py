#Limpando o terminal
from os import system
q = system("cls")

#Exibindo mensagem na tela
print(f"Quer saber quantos reais custa aquele produto que você viu no site de uma Loja Americana ? \nDeixe-me ajudá-lo(a)! \nPara isso, informe o valor do produto em dólares e também o valor atual da taxa de câmbio.")

#Pulando uma linha 
print()

#Solicitando o valor do produto em dólares e convertendo o dado para número decimal
valor_dolar = float(input("Digite o valor do produto em dólares:"))

#Solicitando a taxa de câmbio e convertendo o dado para número decimal
taxa_cambio = float(input("Digite o valor atual da taxa de câmbio:"))

#Calculando o valor do produto em reais
valor_reais = (valor_dolar * taxa_cambio)

#Pulando uma linha 
print()

#Exibindo mensagem na tela 
print(f"Um produto que custa ${valor_dolar} dólares, convertido para reais, acaba custando R${valor_reais} reais.")