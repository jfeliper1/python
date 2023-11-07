from os import system
system ('cls')

n = int(input('Qual termo deseja encontrar?'))
primeiro=1
segundo=1

if (n==1) or (n==2):
    print('1')
else:
    au=1,618
    
    while au <= n:
        termo = primeiro - segundo 
        segundo = primeiro
        primeiro = termo
        au +=1
    print(termo)