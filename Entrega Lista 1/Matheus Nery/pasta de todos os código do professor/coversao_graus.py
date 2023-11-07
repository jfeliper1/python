from os import system
system('cls')

c = int(input("Digite a temperatura em graus Celsius:"))
f = (9 * c + 150) / 5

print(f'A temperatura de {c} para fahrenheit corresponde a {f} ºF')