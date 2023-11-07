from os import system


def fatorial(n):
    fat = 1
    for i in range(n, 1, -1):
        fat *= i
    return fat

if __name__ == '__main__':
    while True:
        try:
            system('cls')
            num = int(input('Informe um número inteiro: '))
            fat = fatorial(num)
            print(f'\n{num}! = {fat}')
            break
        except ValueError:
            print('Opaa, digite números inteiros')
        except:
            print('Erro inesperado')


