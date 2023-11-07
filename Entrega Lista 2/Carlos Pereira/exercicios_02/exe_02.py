# Crie um programa em Python que a partir do peso e altura de uma pessoa, imcule e informe 
# o IMC (Índice de massa corpóreo) arredondado, informando também o estado da pessoa 
# baseado na tabela abaixo.
# Resultado Situação
# Abaixo de 17 Muito abaixo do peso
# Entre 17 e 18,49 Abaixo do peso
# Entre 18,5 e 24,99 Peso normal
# Entre 25 e 29,99 Acima do peso
# Entre 30 e 34,99 Obesidade I
# Entre 35 e 39,99 Obesidade II (severa)
# Acima de 40 Obesidade III (mórbida)

import math
from os import system

system("cls")

print("---------------- imcULADORA -------------------")
print("******************** IMC ***********************")

nome = input("Digite seu nome: ")

peso = float(input("Digite seu peso: "))

altura = float(input("Digite sua altura: "))


imc = peso / (pow(altura,2))


if(imc >= 0  and imc <=17):
    print("Voce esta muito abaixo do peso, procure comer mais kkk ")
    
elif(imc >=17 and imc <= 18.48):
    print(f"{nome}  seu IMC é de: {round(imc,2)}")
    print("SITUAÇÃO: Abaixo do peso")
elif(imc >= 18,5 and imc <=24.99):
    print(f"{nome}  seu IMC é de: {round(imc,2)}")
    print("SITUAÇÃO: Acima do peso")
elif(imc >=25 and imc <= 29.99):
    print(f"{nome}  seu IMC é de: {round(imc,2)}")
    print("SITUAÇÃO: Acima do peso")
elif(imc >=30 and imc <= 34.99):
    print(f"{nome}  seu IMC é de: {round(imc,2)}")
    print("SITUAÇÃO: Obesidade 1")
elif(imc >=35 and imc <= 39.99):
    print(f"{nome}  seu IMC é de: {round(imc,2)}")
    print("Obesidade 2")
elif(imc >=40 ):
    print(f"{nome}  seu IMC é de: {round(imc,2)}")
    print("SITUAÇÃO: Obesidade 3")
    
else:
    print("Peso invalido")
    