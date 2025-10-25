#Haz un programa en Python que calcule el perímetro de una circunferencia con base en su radio.

import math


def calcular_perimetro_circunferencia(radio):
    perimetro = 2 * math.pi * radio
    return perimetro
radio = float(input("Introduce el radio de la circunferencia: "))
perimetro = calcular_perimetro_circunferencia(radio)
print(f"El perímetro de la circunferencia con radio {radio} es: {perimetro:.2f}")