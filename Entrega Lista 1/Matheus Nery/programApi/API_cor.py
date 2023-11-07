from click import clear
import requests, json

def via_cep(cep):
    try:
        req = requests.get(f'https://viacep.com.br/ws/{cep}/json')
        req = req.json()
        return req
    except:
        return -1

if __name__ == '__main__':
    clear()
    try:
        nome = input('\nInforme seu nome: ')
        cep = input('\nInforme o cep: ')
        requisicao = via_cep(cep)
        if requisicao !=-1:
            print('\n*** Dados Pessoais **\n')
            print(f'\nNome: {nome}')
            print(f"Endereço: {requisicao['logradouro']}")
            print(f"Bairro: {requisicao['localidade']}")
            print(f"Estado: {requisicao['uf']}")
        else:
            print('\n** CEP inválido **\n')
    except KeyError: 
        print('\n** CEP inválido **')
    except:
        print('\n** CEP inválido **')


