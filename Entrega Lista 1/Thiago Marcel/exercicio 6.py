valor = float(input("Qual o valor desse produto? "))
desconto = float(input("Qual o valor do desconto? "))
porcentagem = (valor * desconto) / 100


print(f"Voce tera {porcentagem:.2f} reais de desconto")
