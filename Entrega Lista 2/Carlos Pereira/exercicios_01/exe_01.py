# . Crie um programa em Python que solicite o valor da base e altura e calcule a área de um 
# retângulo, apresentando no final todos os valores na tela.
# area_retangulo = base x altura


print("CALCULADORA DA AREA DO RETANGULO")
base = float(input("Digite o valor da base: "))
altura =  float(input("Digite a altura: "))

area = base * altura

print(f"A area do rentangulo com base: {base:.0f} e altura: {altura:.0f} é de: {area:.0f}")