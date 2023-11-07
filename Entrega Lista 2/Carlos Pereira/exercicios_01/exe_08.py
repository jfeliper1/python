# Crie um programa em Python para converter e exibir uma temperatura de graus Celsius para 
# graus Fahrenheit
# 𝐹 = 9 ∗ 𝐶 + 150 / 5

Celsius =  float(input("Digite a temperatura em graus celsius: "))


Fahrenheit = ( (Celsius * ( 9 / 5)) + 32) 

print(f" A conversão de graus celsius para Fahrenheit é de: {Fahrenheit:.0f}")