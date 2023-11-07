# 7. Crie um programa em Python que faça a conversão de um valor em Dólar [USA] para o seu 
# equivalente em Real. Deve ser informada a taxa de câmbio e o valor em dólar para a 
# conversão

dolar = float(input("Informe a quantidade de dólar para conversão: US$ "))
cotacao = float(input ("Informe o valor da cotação do dólar: R$ "))
conversao = dolar*cotacao
print(f"A quantidade de dólar convertido em real é: R${conversao}")