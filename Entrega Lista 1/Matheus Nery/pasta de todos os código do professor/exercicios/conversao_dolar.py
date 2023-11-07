
valor_dolar = float(input("Digite o valor em dólar: "))
taxa_cambio = float(input("Digite a taxa de câmbio (valor do dólar em reais): "))


valor_reais = valor_dolar * taxa_cambio

print(f"Valor em dólar: ${valor_dolar:.2f}")
print(f"Taxa de câmbio: R${taxa_cambio:.2f}")
print(f"Valor equivalente em reais: R${valor_reais:.2f}")





