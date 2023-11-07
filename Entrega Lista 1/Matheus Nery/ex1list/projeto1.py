'''programa que adiciona, mostra, remove, apaga e sai de uma lista'''
from os import system


lista = []
    
def menu():
    system('cls')
    print('\n***Faça sua escolha***\n')
    print('\nEscolha :\n')
    print('1. Adicionar item à lista')
    print('2. Mostrar todos os itens da lista')
    print('3. Remover item da lista')
    print('4. Apagar todos os itens da lista')
    print('5. Sair')
    op = int(input('\nOpção: '))
    return op

     

def adicionar(item1):
    add = [item1]
    lista = add
    return()

def remover():
    lista = lista.remove(item1)


def guardar():
    lista(lista)

if __name__ == '__main__':
    op = menu()
  
    match op:
        case 1:
            item1 = str(input('Informe o item à ser adicionado: '))
            add = adicionar(item1)
            menu()
            
        case 2:
            print(f'Segue itens adicionados à lista:')
            adicionar(lista)
                
           
        
       
            

            


   

    
    




    

