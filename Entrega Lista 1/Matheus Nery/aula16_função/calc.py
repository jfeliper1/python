from os import system
#função para somar 

    

def menu():
    system('cls')
    print('\n***Calculadora Smart***\n')
    print('\nEscolha :\n')
    print('1. Soma')
    print('2. Subtrair')
    print('3. Multiplicação')
    print('4. Divisão')
    op = int(input('\nOpção: '))
    return op



def entrada():
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    return n1, n2 



def saida(n1, n2, resultado, sinal):
    print(f'\n{n1} {sinal} {n2} = {resultado}')




def somar(n1, n2):
    saida(n1, n2, n1 + n2, '+')




def subtrair(n1, n2):
    saida(n1, n2, n1 - n2, '-')


def multiplicar(n1, n2):
    saida(n1, n2, n1 * n2, 'x')


def dividir(n1, n2):
    saida(n1, n2, n1 / n2, '/')


if __name__ == '__main__':
    op = menu() # <--- O retorno vai para quem o chamou.
    n1, n2 = entrada()


    match op:
        case 1:
            somar(n1, n2)
        case 2:
            subtrair(n1, n2)
        case 3:
            multiplicar(n1, n2)
        case 4:
            dividir(n1, n2)
        case _:
            print('\nOpção invalida, digite um número válido\n') 

            menu()
            
