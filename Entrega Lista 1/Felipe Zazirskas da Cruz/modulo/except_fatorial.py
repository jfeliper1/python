from click import clear

def fatorial(n):
    fat = 1

    for i in range(n, 1, -1):
        fat *=i
    return fat


if __name__ == '__main__':
    clear()
    while True:
        try:
          num = int(input('\n\n Informe um nº inteiro : '))
          fat = fatorial(num)
          print(f'\n\n{num}! = {fat}\n\n')
          break
        except ValueError:
             print('\n Ops, somente nros inteiros são aceitos.\n\n')
        except:
             print('\n  Erro inesperado.\n\n')
