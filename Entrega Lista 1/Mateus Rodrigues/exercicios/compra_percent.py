initial_value = float(input('Digite o valor inicial da compra: '))
discount_percent = int(input('Digite o desconto percentual (em %): '))

discount = (discount_percent / 100) * initial_value

final_value = initial_value - discount

print(f'O valor final da compra apóa o desconto de {discount_percent} é: R${final_value}')