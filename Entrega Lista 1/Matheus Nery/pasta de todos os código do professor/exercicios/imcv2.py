from os import system
system('cls')

#Solicita o peso em quilogramas e a altura em metros
peso = float(input("Digite seu peso (em kg): "))
altura = float(input("Digite sua altura (em metros): "))

# Calcula o IMC
imc = peso / (altura ** 2)

# Arredonda o IMC para duas casas decimais
imc_arredondado = round(imc, 2)

# Determina a situação com base no IMC
if imc < 17:
    situacao = "Muito abaixo do peso"
elif 17 <= imc < 18.5:
    situacao = "Abaixo do peso"
elif 18.5 <= imc < 25:
    situacao = "Peso normal"
elif 25 <= imc < 30:
    situacao = "Acima do peso"
elif 30 <= imc < 35:
    situacao = "Obesidade I"
elif 35 <= imc < 40:
    situacao = "Obesidade II (severa)"
else:
    situacao = "Obesidade III (mórbida)"

# Exibe o IMC arredondado e a situação da pessoa
print("Seu IMC é: " + str(imc_arredondado))
print("Sua situação é: " + situacao)


