start = int(input('Digite o primeiro número do intervalo: '))
end = int(input('Digite o ultimo número do intervalo: '))
  
for i in range(start, end+1): 
  if i>1: 
    for j in range(2,i): 
        if(i % j==0): 
            break
    else: 
        print(i)


