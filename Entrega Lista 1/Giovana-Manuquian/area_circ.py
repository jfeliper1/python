from math import pi
from os import system

system('cls')

raio = float(input("Digite a área: "))
area_circ = pi * (raio**2)
print(f"A circunferência de um círculo com raio {raio} é {area_circ:.2f}")