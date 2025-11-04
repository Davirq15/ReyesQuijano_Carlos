# Haz un programa que solicite números al usuario hasta que ingrese un cero.
# Al final, imprime cuántos números positivos y negativos introdujo.

contadorP = 0
contadorN = 0

inicio = input("Presiona Enter para iniciar el conteo...")

while True:
    numero = int(input("Ingresa un número (Escribe ¨0¨ para salir): "))
    if numero == 0:
        break
    elif numero > 0:
        contadorP += 1
    else:
        contadorN += 1
print(f"Total de números positivos ingresados: {contadorP}")
print(f"Total de números negativos ingresados: {contadorN}")