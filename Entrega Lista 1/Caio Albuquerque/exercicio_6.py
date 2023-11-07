valor_compra   = float(input("Digite o valor da compra:R$ "))
valor_desconto = float(input("Digite o valor do desconto: ")) 
valor_final    = (valor_compra * valor_desconto) / 100
economizado    = valor_compra - valor_final 
print(f"O valor da compra com {valor_desconto}% de desconto e com uma economia de R${valor_final} é de: R${economizado}")
