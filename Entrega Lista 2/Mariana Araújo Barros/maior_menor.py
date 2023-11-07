idade = int(input("Digite a sua idade: "))


if(idade >0 and idade <=120):
    if( idade >18):
        print("Você é maior de idade")
    else: print("Você é menor de idade, acesso barrado!")
else:
    print("Idade inválida")

