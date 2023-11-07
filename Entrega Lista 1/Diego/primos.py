from os import system
system ('cls')

n1= int(input('Digite um número para saber se ele é primo: '))
n=0

for i in range(n1-1,2,-1):
    if(n1/i).is_integer()== True:
        n+=1

if n == 0:
    print(n1,'É primo')
else:
    print('Não é primo')
