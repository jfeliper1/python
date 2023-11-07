numero= int(input('Fatorial de: '))
resultado = 1
fat= 1
while 0 <= fat:
    resultado*= fat
    fat+=1
if resultado !=1:
    print(resultado)
else:
    print('Fim')