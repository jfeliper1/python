# Segunda-feira caso o número digitado seja 1
# Terça-feira-feira caso o número digitado seja 2
# ...
# Sábado caso o número digitado seja 6
# Domingo caso o número digitado seja 7

dia = int(input("Informe um número entre 1 e 7: "))

if dia >0 and dia == 1:
    print("Hoje é segunda-feira")
elif dia == 2:
    print("Hoje é terça-feira")
elif dia == 3:
    print("Hoje é quarta-feira")
elif dia == 4:
    print("Hoje é quinta-feira")
elif dia == 5:
    print("Hoje é sexta-feira")
elif dia == 6:
    print("Hoje é sábado")
elif dia == 7:
    print("Hoje é domingo")
else:
    print("Valor inválido!!!!")


# dia = {
#     1: print("Hoje é segunda-feira"),
#     2: print("Hoje é terça-feira"),
#     3: print("Hoje é quarta-feira"),
#     4:print("Hoje é quinta-feira"),
#     5: print("Hoje é sexta-feira"),
#     6: print("Hoje é sábado"),
#     7: print("Hoje é quarta-feira")
# }