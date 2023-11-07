import math

num_1 = float(input("Digite o primeiro valor: "))
num_2 = float(input("Digite o segundo valor: "))

soma          = num_1 + num_2
subtracao     = num_1 - num_2
multiplicacao = num_1 * num_2
divisao  = num_1 / num_2
potencia = num_1**num_2
modulo   = num_1 % num_2
raiz_1   = math.sqrt(num_1)
raiz_2   = math.sqrt(num_2)

print("Aqui está estes dois valores em diferentes calculos matematicos \n" +
 f"soma {soma} \n "+
 f"subtracao {subtracao} \n "+
 f"multiplicacao {multiplicacao} \n "+ 
 f"divisao {divisao} \n "+
 f"potencia {potencia} \n "+
 f"modulo {modulo} \n "+
 f"raiz 1 {raiz_1} \n "+
 f"raiz 2{raiz_2}")