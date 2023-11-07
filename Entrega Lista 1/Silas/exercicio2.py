#1. . Crie um programa em Python que solicite o valor da base e altura e calcule a área de um 
#triângulo, apresentando no final todos os valores na tela. 
#area_triangulo = base x altura / 2

base= float(input("digite o valor da base: "))

altura= float(input("digite o valor da altura: "))

area_triangulo= base * altura /2

print (f'O valor da base é: {base}\n O valor da altura é: {altura}')
print (f'Portanto, o valor da área do seu triangulo é: {area_triangulo}')