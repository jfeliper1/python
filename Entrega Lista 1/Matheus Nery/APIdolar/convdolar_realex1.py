from click import clear
import requests, json
from datetime import date

def taxa():
    try:
        req = requests.get(f'https://economia.awesomeapi.com.br/last/USD-BRL')
        req = req.json()
        return float((req['USDBRL']['bid']))
    except:
        return -1 
        
        

if __name__ == '__main__':
    try:
        clear()
        dolar = float(input('\nQuantidade de dolar para converter: U$'))
        tx = taxa()
        if tx != -1:
            real = dolar * tx
            data = data.today()
            data_br = f'{data.day}/{data.month}/{data.year}'
            print(f'\nTaxa do dolar em {data_br}: R${round(tx, 2)}')
            print(f'U$ {dolar} equivalente R$ {round(real, 2)}\n')
        else:
            print('\nErro inesperado\n')
    except:
        print('\nErro inesperado\n')
    


