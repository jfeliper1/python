# Limpar a tela:
from os import system
system("cls")

num = int(input("Informe um número inteiro: "))

if (num != 0) :
    if(num <0):
        print(f'\n{num} é negativo\n')
        
    else:
        print(f'\n{num} é positivo\n')

else: 
    print(f'\n{num} possui o atributo neutro')
 
    
 
