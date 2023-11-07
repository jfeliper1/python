from os import system

system('cls')

preco_prod = float(input('Informe o preço do produto?'))
desconto = float(input('Valor do desconto?'))

desconto_monetario = (preco_prod * desconto) / 100
valor_final = preco_prod - desconto_monetario

print(f'Preço do produto: R$ {preco_prod}')
print(f'% de desconto: {desconto}')
print(f'Valor a pagar: R$ {valor_final}\n')

