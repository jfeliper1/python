# . Crie um programa em Python que solicite o valor da base e altura e calcule a área de um 
# triângulo, apresentando no final todos os valores na tela.
# area_triangulo = base x altura / 2


print("CALCULADORA DA AREA DO TRIANGULO")
base = float(input("Digite o valor da base: "))
altura =  float(input("Digite a altura: "))

area = (base * altura) / 2

print(f"A area do Triangulo com base: {base:.0f} e altura: {altura:.0f} é de: {area:.0f}")