import requests, json

cep = '08275-450'
req = requests.get(f'https://viacep.com.br/ws/{cep}/json')
req = req.json()
print(req)

print(f'req["bairro"]')