import math 

n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))

soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
potencia = n1**n2
modulo = n1 % n2
raiz1 = math.sqrt(n1)
raiz2 = math.sqrt(n2)

print(f"A soma dos dois números é: {soma}\n" +
      f"A subtração dos dois números é: {subtracao}\n" +
      f"A multiplicação dos dois números é: {multiplicacao}\n" +
      f"A divisão dos dois números é: {divisao}\n" +
      f"A potência dos dois números é: {divisao}\n" +
      f"O módulo dos dois números é: {divisao}\n" +
      f"A raíz desse desse número é: {raiz1}\n" +
      f"A raíz desse número é: {raiz2}\n"
      )


