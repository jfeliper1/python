import math

n1= float(input('\n\t\tInforme o valor de N1:'))
n2= float(input('\n\t\tInforme o valor de N2:'))
soma= n1 + n2
subtracao= n1-n2
multiplicacao= n1*n2
divisao= n1/n2
potencia=n1**n2
raizn1=math.sqrt(n1) 
raizn2=math.sqrt(n2)
print(f'\n\t\tA soma de N1+N2 é {soma}')
print(f'\n\t\tA subtracação de N1-N2 é {subtracao}')
print(f'\n\t\tA multiplicação de N1*N2 é {multiplicacao}')
print(f'\n\t\tA divisão de N1/N2 é {divisao}')
print(f'\n\t\tA potencia entre N1**N2 é {potencia}')
print(f'\n\t\tA raiz quadrada de N1 é {raizn1}')
print(f'\n\t\tA raiz quadrada de N2 é {raizn2}')

peso=float(input("\n\t\tdigite seu peso em Kg:"))
altura=float(input("\n\t\tdigite sua altura:"))
imc=peso/math.pow(altura,2)
print(f'\n\n\t\tPeso:{peso}\n\n\t\tAltura:{altura}\n\n\t\tImc:{round(imc, 3)}\n\n')

raio= float(input('\n\n\t\tInforme o valor do raio :'))
area_circ=math.pi*(raio**2)
print(f'\n\n\t\tA area do circulo é:{area_circ} ')

base= float(input("\n\n\t\tInfome o valor da base do triangulo :"))
altura= float(input("\n\n\t\tInfome o valor da altura do triangulo :"))
area= base*altura
print(f'\n\n\t\t O valor da área do triangulo é {area}\n\n')

base= float(input("\n\n\t\tInfome o valor da base do triangulo :"))
altura= float(input("\n\n\t\tInfome o valor da altura do triangulo :"))
area= (base*altura)/2
print(f'\n\n\t\t O valor da área do triangulo é {area}\n\n')

raio= float(input("\n\n\t\t Informe o raio da circunferencia :"))
perimetro_circ= math.pi * 2 * raio
print(f"\n\n\t\tO valor do perimetro é{perimetro_circ}")

raio= float(input('\n\n\t\tInforme o valor do raio :'))
area_circ=math.pi*(raio**2)
print(f'\n\n\t\tA area do circulo é:{area_circ} ')

print(f'\n\t\tValor U$ em 27.09.2023: 5,04')
dolar= float(input(f'\n\t\tInforme o valor para conversão:'))
conversao= dolar* 5.04
print(f'\n\t\t total convertido : {conversao}')

celsius=float(input(f'\n\t\tInforme os graus Celsius: '))
fahrenheit= ((9*celsius) + 150 ) /5
print(f'\n\t\t{celsius}º Celsius equivale a {fahrenheit}º fahrenheit')

print(f'\n\t\tGanhe 30% de desconto nas compras acima de R$ 1000,00 ')
item1= float(input('\n\t\tInforme o valor do item 1 :'))
item2= float(input('\n\t\tInforme o valor do item 2 :'))
item3= float(input('\n\t\tInforme o valor do item 3 :'))
item4= float(input('\n\t\tInforme o valor do item 4 :'))
item5= float(input('\n\t\tInforme o valor do item 5 :'))
total= item1 + item2 + item3 + item4 + item5
total_desc= (item1 + item2 + item3 + item4 + item5) * 0.3
valor_desc= (item1 + item2 + item3 + item4 + item5) * 0.9
print (f' \n\t\tO total da compra foi {total}')
print (f' \n\t\tO total de desconto foi {total_desc}')
print (f' \n\t\tO total a ser pago é {valor_desc}')





