print ("=====================================================")
print ("olá, vamos calcular o perímetro da circunferência ")
print ("=====================================================")

Raio_str = input("Qual é o valor do raio? ")
Raio = float(Raio_str)
Pi = 3.14 

perimetro = (2 * (Pi * Raio))

resultado_format = "{:.2f}".format(perimetro)




print ("=====================================================")
print (F"O perímetro da circunferencia é {resultado_format}  ") 
print ("=====================================================")
