from os import system
system('cls')

quantidade = int(input("Digite a quantidade de números na série de Fibonacci: "))

a, b = 0, 1

print("Série de Fibonacci:")
for _ in range(quantidade):
    print(a, end=" ")
    a, b = b, a + b