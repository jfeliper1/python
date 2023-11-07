from os import system
system('cls')

numero = int(input('Insira um número inteiro para ser fatorado:'))

if numero < 0:
    print('não é possível fatorar números negativos')

else:
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    print(f'O fatorial do {numero} é {resultado}')