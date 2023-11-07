# Converte a temperatura de graus celsius para fahrenheit
# Autor: Matheus Nery 
# Data: 28/09/2023
# Versão: 1.0 
from os import system

system('cls') # <-Essa é ordem de limpar a tela 

c = float(input('Informe a temperatura em ºCelsius:'))

f = (9*c + 150) / 5 # <- Formula para calcular a temperatura Cº para Fahrenheit 

print(f'{c}ºCelsius equivale a {f} ºFahrenheit')
