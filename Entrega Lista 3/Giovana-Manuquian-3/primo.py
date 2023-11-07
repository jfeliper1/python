from os import system
system('cls')


numero = int(input("Digite um número inteiro maior que [1]: "))

if numero > 1:
   
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            print(f"O {numero} não é um número primo.")
            break
    else:
        print(f"O {numero} é um número primo.")
else:
    print("Por favor, digite um número maior que '1'.")