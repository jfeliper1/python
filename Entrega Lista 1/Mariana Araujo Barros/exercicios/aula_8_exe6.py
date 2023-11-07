# 6. Crie um programa em Python para calcular o valor final de uma compra, com desconto 
# percentual qualquer

valor_compra = float(input(f"Digite o valor da compra: "))
desconto = int(input(f"Informe a porcentagem do desconto: "))

percentual = desconto / 100

total_compra = valor_compra * (1 - percentual)

print(f"O valor final da compra é: {total_compra}")
