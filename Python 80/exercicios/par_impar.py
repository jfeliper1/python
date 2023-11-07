from os import system
system('cls')



 #Obtém a entrada do usuário
numero = input("Digite um número inteiro positivo diferente de 0: ")

# Verifica se a entrada é um número inteiro positivo
if numero.isdigit():
    numero = int(numero)
    # Verifica se o número é diferente de 0 e positivo
    if numero > 0:
        # Verifica se o número é par ou ímpar
        if numero % 2 == 0:
            print("O número é par.")
        else:
            print("O número é ímpar.")
    else:
        print("Por favor, digite um número inteiro positivo diferente de 0.")
else:
    print("Por favor, digite um número inteiro positivo válido.")