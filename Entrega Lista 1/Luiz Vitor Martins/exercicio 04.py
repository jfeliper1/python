print ("=====================================================")
print ("olá, vamos calcular a área da circunferência ")
print ("=====================================================")

Raio_str = input("Qual é o valor do raio? ")
Raio = float(Raio_str)
Pi = 3.14 

area = (Pi * (Raio * Raio))

resultado_format = "{:.2f}".format(area)




print ("=====================================================")
print (F"A área da circunferência é {resultado_format}  ") 
print ("=====================================================")