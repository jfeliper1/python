from os import system

system('cls')

phrase_user = input("Digite a frase que você quer no centro da moldura: ")
ch = '\u2588' # char

tamanho_frase = len(phrase_user)
largura_moldura = tamanho_frase + 4

print(f'{ch}' * largura_moldura)

for i in range(2):
    if i == 0:
        print(f'{ch} ' + phrase_user + f' {ch}')
    else:
        print(f'{ch}' * largura_moldura)