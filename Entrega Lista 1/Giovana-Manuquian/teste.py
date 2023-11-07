peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
resultado = peso / (altura **2)
print(f'O seu peso é {peso}, sua altura é {altura} e seu IMC é {round(resultado, 1)}')