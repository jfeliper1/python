from os import system
system('cls')

quantidade = int(input("Digite a quantidade de números na série de Fibonacci: "))

a, b = 1, 1

phi = 1.618

print("Série de Fibonacci com números áureos:")
for i in range(quantidade):
    print(a, end=" ")
    if i % 2 == 0:
        print(f"(Áureo: {b * phi:.3f})", end=" ")
    a, b = b, a + b