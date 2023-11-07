from os import system
system('cls') or system('clear')

n = int(input('Informe o dia da semana [1...7]:'))

match n: 
    case 1:
        print('\nSegunda - feira')
    case 2:
        print('\nTerça - Feira')
    case 3:
        print('Quarta - Feira')
    case 4:
        print('Quinta - feira')
    case 5:
        print('Sexta - Feira')
    case 6:
        print('Sábado')
    case 7: 
        print('Domingo')
    case _:
        print('Opção inválida')
        
