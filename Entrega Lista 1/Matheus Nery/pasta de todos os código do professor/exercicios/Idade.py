from os import system
system('cls')

age = int(input('Insira a idade para validação:'))

if 0<= age <=120:
    if age >= 18:
        print(f'com {age} anos, você já é maior de idade')
    else:
        print(f'com {age} anos, você é menor de idade')

else: 
    print(f'Insira uma idade válida')

