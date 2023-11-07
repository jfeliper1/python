
valor_original = float(input("Digite o valor da compra: "))
desconto_percentual = float(input("Digite o desconto percentual (%): "))

desconto = (desconto_percentual / 100) * valor_original

valor_final = valor_original - desconto

print(f"Valor final da compra com {desconto_percentual}% de desconto: R${valor_final:.2f}")
