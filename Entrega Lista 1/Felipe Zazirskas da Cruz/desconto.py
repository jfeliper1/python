print(f'\n\t\tGanhe 30% de desconto nas compras acima de R$ 1000,00 ')
item1= float(input('\n\t\tInforme o valor do item 1 :'))
item2= float(input('\n\t\tInforme o valor do item 2 :'))
item3= float(input('\n\t\tInforme o valor do item 3 :'))
item4= float(input('\n\t\tInforme o valor do item 4 :'))
item5= float(input('\n\t\tInforme o valor do item 5 :'))
total= item1 + item2 + item3 + item4 + item5
total_desc= (item1 + item2 + item3 + item4 + item5) * 0.3
valor_desc= (item1 + item2 + item3 + item4 + item5) * 0.9
print (f' \n\t\tO total da compra foi {total}')
print (f' \n\t\tO total de desconto foi {total_desc}')
print (f' \n\t\tO total a ser pago é {valor_desc}')































