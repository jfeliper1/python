#Limpando a tela
from os import system
a = system ("cls")

#Solicitando que o usuário informe um número 
n_day = int(input("Informe o dia da semana [1...7]: "))

#Verificando o dia da semana relacionado ao número 
if n_day <1:
    print (f"\nNúmero inválido\n")
else:
    if n_day >7:
        print (f"\nnúmero inválido\n")
    else: 
        if n_day == 1:
            print (f"\nSegunda-Feira\n")
        else:
            if n_day == 2:
                print (f"\nTerça-Feira\n")
            else:
                if n_day == 3:
                    print (f"\nQuarta-Feira\n")
                else:
                    if n_day == 4:
                        print(f"\nQuinta-Feira\n")
                    else:
                        if n_day == 5:
                            print(f"\nSexta-Feira\n")
                        else:
                            if n_day == 6:
                                print(f"\nSábado\n")
                            else:
                                print (f"\nDomingo\n")
