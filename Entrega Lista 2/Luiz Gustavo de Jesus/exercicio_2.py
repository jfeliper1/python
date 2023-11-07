#Limpando a tela
from os import system
a = system ("cls")

#Solicitando altura do usuário
altura = float(input("Informe a sua altura: "))
peso = float(input("\nInforme o seu peso: "))

#Calculando o indice de massa corpóreo do usuário
imc = peso / altura**2 

#Verificando se o usuário está muito abaixo do peso 
if imc <17:
    print(f"\nSeu imc é {round(imc,2)}, você está muito abaixo do peso\n")
else: 
    if imc >= 17:
        if imc <= 18.49:
            print(f"\nSeu imc é: {round(imc,2)}, você está abaixo do peso\n")
        else:
            if imc >= 18.5:
                if imc <= 24.99:
                    print(f"\nSeu imc é: {round(imc,2)}, você está com o peso normal.\n")
                else:
                    if imc >= 25: 
                        if imc <= 29.99:
                            print (f"\nSeu imc é {round(imc,2)}, você está acima do peso.\n")
                        else:
                            if imc >= 30: 
                                if imc <= 34.99:
                                    print(f"\nSeu imc é: {round(imc,2)}, você está com obesidade I\n")
                                else:
                                    if imc >= 35:
                                        if imc <= 39.99:
                                            print(f"\nSeu imc é: {round(imc,2)}, você está com obesidade II(severa).\n")
                                        else: 
                                            if imc >= 40:
                                                print (f"\nSeu imc é: {round(imc,2)}, você está com obesidade III(mórbida).\n")
                                        



