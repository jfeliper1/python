from click import clear
import requests, json
from datetime import date


def taxa():
    try:
        req = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
        req = req.json()
        return float((req['USDBRL']['bid']))
    except:
        return -1


if __name__=='__main__':
    try:
        clear()
        dolar = float(input('\n USD: '))
        tx = taxa()
        if tx != -1:
            real = dolar * tx
            data = date.today()
            data_br = f"{data.day}/{data.month}/{data.year}"
            print(f'\n TX USD em {data_br} : R${round(tx, 2)}\n')
            print(f'\nUSD {dolar} equivale R$ {round(real, 2)}\n')
        else:
            print('\n ***ERRO***')
    except:
        print('\n ***Erro***')