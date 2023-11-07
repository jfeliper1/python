from click import clear
import requests, json

def via_cep(cep):
    try:
        req = requests.get(f'https://viacep.com.br/ws/{cep}/json')
        req = req.json()
        print(req)
        return req
    except:
        return -1


if __name__=='__main__':
    try:
        clear()
        nome = input('\n Informe seu nome:  ')
        cep = input('\n Informe seu cep:  ')
        requisicao = via_cep(cep)
        if requisicao != -1:
            print("\n ** DADOS PESSOAIS ** \n ")
            print(f"\n Nome:{nome}")
            print(f"\n Endereço: {requisicao['logradouro']} ")
            print(f"\n Bairro: {requisicao['bairro']}")
            print(f"\n Cidade: {requisicao['localidade']}")
            print(f"\n Uf: {requisicao['uf']}\n")
        else :
            print('\n ***Cep invalido***\n')
    except KeyError:
         print('\n *** Cep invalido***\n')
    except:
         print('\n ***Cep invalido***\n')


   
