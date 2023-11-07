# 7. Crie um programa em Python que faça a conversão de um valor em Dólar [USA] para o seu 
# equivalente em Real. Deve ser informada a taxa de câmbio e o valor em dólar para a 
# conversão.


Valor_em_Dolar = float(input("Digite o valor em Dolar que será trocado: "))
Taxa_Cambio = float(input("Digite a taxa de conversão atual: "))

Valor_Reais = Valor_em_Dolar * Taxa_Cambio


print(f'O montante de dolares totalizou em: USD {Valor_em_Dolar},\na Taxa de Conversão na data era de: R$ {Taxa_Cambio},\nO valor em Reais foi de: R$ {Valor_Reais}.')