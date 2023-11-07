from os import system
system ('cls')

n = int(input('Qual termo deseja encontrar?: '))
ultimo=1
penultimo=1

if (n==1) or (n==2):
    print('1')
else:
    fat=3
    
    while fat <= n:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        fat +=1
    print(termo)
