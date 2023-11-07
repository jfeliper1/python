import math

peso = float(input("Digite o seu peso: "))
altura = float(input("Informe a sua altura: "))

imc = peso / (altura ** 2)

if imc >=0 and imc <= 17:
     print(f"{imc} - Muito abaixo do peso ") 
elif imc  >= 17 and imc <= 18.49:
        print(f"{round(imc, 2)} - Abaixo do peso")
elif imc  >= 18.55 and imc <= 24.99:
        print(f"{round(imc, 2)} - Peso Normal")
elif imc  >= 25 and imc <= 29.99:
        print(f"{round(imc, 2)} - Acima do peso")
elif imc  >= 30 and imc <= 34.99:
        print(f"{round(imc, 2)} - Obesidade 1")
elif imc  >= 35 and imc <= 39.99:
        print(f"{round(imc, 2)} - Obesidade 2 (severa)")
elif imc  > 40:
        print(f"{round(imc, 2)} - Obesidade 3 (mórbida)")
else:
      print("Dados inválidos") 