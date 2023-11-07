n=int(input(f'Informe um número entre 1 e 7:'))

if n>0:
    if n<=7:
        if n==1:
            print(f'\n\n\t\tSegunda-Feira')
        else:
            if n==2:
                print(f'\n\n\t\tTerça-Feira')    
            else:
                if n==3:
                    print(f'\n\n\t\tQuarta-Feira')    
                else:
                    if n==4:
                        print(f'\n\n\t\tQuinta-Feira')    
                    else:    
                        if n==5:
                            print(f'\n\n\t\tSexta-Feira')
                        else:
                            if n==6:
                                print(f'\n\n\t\tSabado.')    
                            else:
                                print(f'\n\n\t\tDomingo.')
    else:
        print(f'\n\n\t\tValor invalido.')
else:
    print(f'\n\n\t\tValor invalido.')
       
        



