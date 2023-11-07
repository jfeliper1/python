print ("=====================================================")
n1 = float(input("digite um número: "))
n2 = float(input("digite outro número: "))
print ("=====================================================")
soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
potencia = n1 ** n2
import math
raizN1 = math.sqrt(n1)
raizN2 = math.sqrt(n2)

print ("=====================================================")
print(f"A soma dos dois numeros é {soma}")
print(f"A subtração dos dois numeros é {subtracao}")
print(f"A multiplicação dos dois numeros é {multiplicacao}")
print(f"A divisão dos dois numeros {divisao:.2f}")
print(f"A potência do primeiro valor elevado pelo segundo valor é {potencia:.2f}")
print(f"\nA raiz quadrada de {n1} é {raizN1:.2f}")
print(f"\nA raiz quadrada de {n2} é {raizN2:.2f}")
print ("=====================================================")