# Pide una palabra y reemplaza todas las vocales por el simbolo *

palabra = input("Ingresa una palabra: ")
vocales = "aeiouAEIOU"
simbolo = ""

for letra in palabra:
    if letra in vocales:
        simbolo += "*"
    else:
        simbolo += letra
print(f"La palabra ahora cambiada con el simbolo es: {simbolo}")