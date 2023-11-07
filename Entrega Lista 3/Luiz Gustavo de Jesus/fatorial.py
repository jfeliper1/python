n = int(input(f"\nDigite um número inteiro positivo: "))
fatorial = 1

while n <= 0:
    n = int(input(f"\nDigite um número inteiro positivo: "))

for i in range(1,n+1):
    fatorial *= i
   
print (f"{fatorial}")
