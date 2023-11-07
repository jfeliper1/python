
from os import system

def menu():
    system('cls')
    print('******************Calculadora******************')
    print('Escolha uma das opções a seguir: ')
    print('1 - Somar')
    print('2 - Subtrair')
    print('3 - Multiplicar')
    print('4 - Dividir')
    
    while True:
        try:
            op = int(input('Opção: '))
            if 1 <= op <= 4:
                break
            else:
                print("Opção inválida. Escolha uma opção de 1 a 4.")
        except ValueError:
            print("Opção inválida. Escolha uma opção de 1 a 4.")
    
    print('*************************************************')
    return op

def entrada():
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    return n1, n2

def somar(n1, n2):
    resultado = n1 + n2
    print(f'O resultado da conta é: {resultado}')

def subtrair(n1, n2):
    resultado = n1 - n2
    print(f'O resultado da conta é: {resultado}')

def multiplicar(n1, n2):
    resultado = n1 * n2
    print(f'O resultado da conta é: {resultado}')

def dividir(n1, n2):
    resultado = n1 / n2
    print(f'O resultado da conta é: {resultado}')

if __name__ == '__main__':
    op = menu()
    num1, num2 = entrada()

    match op:
        case 1:
            somar(num1, num2)
        case 2:
            subtrair(num1, num2)
        case 3:
            multiplicar(num1, num2)
        case 4:
            dividir(num1, num2)

        

 
            
            

 