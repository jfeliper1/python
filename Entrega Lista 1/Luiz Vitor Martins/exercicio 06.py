print ("=====================================================")
print ("olá, vamos calcular o seu desconto ")
print ("=====================================================")

Valor_str = input("Qual é o valor do produto/serviço? ")
Valor = float(Valor_str)
Desconto_str = input("quanto de desconto? ")
Desconto = float(Desconto_str)
porcentagem = (Desconto * Valor) / 100

resultado_format = "{:.2f}".format(porcentagem)




print ("=====================================================")
print (F"Você terá {resultado_format} reais de desconto ") 
print ("=====================================================")