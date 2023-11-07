# Crie um programa em Python para calcular o valor final de uma compra, com desconto 
# percentual qualquer.

valor = float(input("Digite o valor total da compra: "))
desconto = 10 * (valor / 100)
valor_com_desconto = valor - desconto

print("##########################################")
print(f"PARABÉNS!!! VOCÊ RECEBEU 10% DE DESCONTO")
print(f"O valor total da sua compra com desconto foi de: {valor_com_desconto:.2f}")
print("##########################################")



