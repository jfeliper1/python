# 1. Crie um programa em Python que solicite a idade do usuário e informe se este e menor ou 
# maior de idade. Considere avaliar se a idade é válida, sendo que esta não pode ser menor 
# que zero ou maior que cento e vinte anos.

from os import system

system("cls")

idade = int(input("Digite sua idade: "))
regras = 18
max_idade = 120
min_idade = 1

if(idade >= min_idade and idade <= max_idade):
    if(idade >= regras):
        print("Parabens vc pode entrar balada!!! ")
    else:
        print("Sinto muito vc nao tem idade suficiente para entrar na balada ")
        
else:
    print("IDADE INVALIDA!! ")