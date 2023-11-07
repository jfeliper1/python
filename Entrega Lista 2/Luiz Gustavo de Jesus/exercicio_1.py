'''
Crie um programa em Python que solicite a idade do usuário e informe se este e menor ou 
maior de idade. Considere avaliar se a idade é válida, sendo que esta não pode ser menor 
que zero ou maior que cento e vinte anos

'''
#Solicitando a idade do usuário 
idade = int(input("Informe sua idade: "))

#Criando uma regra para que não sejam aceitas idades <0 e >120
# Verificando se a idade digitada é <0:
if idade <= 0:
    print("\nIdade inválida\n")
#Se não for <0, o que fazemos ?
else:
    #Verificamos se a idade digitada é >120:
    if idade >120:
        print("\nIdade inválida\n")
#Caso a idade digitada não seja <0 e >120, o que fazemos ?
    else: 
        #Verificamos se o usuário é menor de idade 
        if idade <= 17:
            print("\nVocê é menor de idade\n")
        #Se o usuário não é menor de idade, o que fazemos ?
        else:
        #Verificamos se o usuário é maior de idade
            if idade >= 18:
                print("\nVocê é maior de idade\n")



