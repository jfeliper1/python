taxa_cambio = float(input('Digite a taxa de câmbio em Dólar para Real: '))
dolar_value = float(input('Digite o valor em dólar: '))

real_value = dolar_value * taxa_cambio

print(f'O valor em Real é de: R${real_value:.2f}')