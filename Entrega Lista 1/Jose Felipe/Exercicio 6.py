# 6. Crie um programa em Python para calcular o valor final de uma compra, com desconto 
# percentual qualquer

Preco_venda = float(input("Digite o Valor Total do Produto antes do desconto: "))
Percentual_desconto = float(input("Digite o % de desconto oferecido: ")) / 100

Desconto = Preco_venda * Percentual_desconto

Preco_apos_descontos = Preco_venda - Desconto

print(f'O Valor original do produto era: R$ {Preco_venda},\nO desconto oferecido foi de: {round((Percentual_desconto * 100),2)}%,\nO Valor total a pagar é de: R$ {Preco_apos_descontos}.')