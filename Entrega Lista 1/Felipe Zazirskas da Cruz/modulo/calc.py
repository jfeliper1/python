from os import system

def menu():
    system('cls')
    print('\n ***Calculadora Betha***\n')
    print('Escolha:\n')
    print('1.Soma\n')
    print('2.Subtração\n')
    print('3.Multiplicação\n')
    print('4.Divisão\n')
    op=int(input('\n Opção:  '))         
    return op 


def entrada():
    n1=float(input('\n Digite o 1º nro : '))
    n2=float(input('\n Digite o 2º nro : '))
    return n1, n2


def saida(n1, n2, resultado, sinal):
    print(f'\n {n1} {sinal} {n2} = {resultado}\n\n')


def somar(n1, n2):
   saida(n1, n2, (n1+n2),'+' )


def subtrair(n1, n2):
    saida(n1, n2, (n1-n2),'-' )    


def dividir(n1, n2):
    saida(n1, n2, (n1/n2),':' ) 
    

def multiplicar(n1, n2):
    saida(n1, n2, (n1*n2),'x' ) 


if __name__=='__main__':
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
        case _:
            menu(num1, num2)
