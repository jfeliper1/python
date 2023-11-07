#8. Crie um programa em Python para converter e exibir uma temperatura de graus Celsius para 
# graus Fahrenheit.
# 𝐹 =
# 9 ∗ 𝐶 + 150

valor= float(input("digite a temperatura em °Celsius a ser convertida em Fahrenheit: "))

F= (9* valor +150)/5

print (f'A temperatura em Celsius a ser convertido é:{valor}°C')
print (f'Logo a temperatura em Fahrenheit : {F}')