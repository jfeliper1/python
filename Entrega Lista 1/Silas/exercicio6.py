#6. Crie um programa em Python para calcular o valor final de uma compra, com desconto percentual qualquer.

valor= float(input("digite o valor do produto: R$"))

desc= float(input("digite o valor da porcentagem de desconto concebido: "))

valor_do_produto= valor - (desc/100 * valor) 

print (f'O valor do produto  é: R${valor}\n A porcentagem de desconto  concebido foi: {desc}%')
print (f'Portanto, o valor pago será: R${valor_do_produto}')