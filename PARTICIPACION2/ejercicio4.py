#  Haz un programa que pida 5 números (Técnicamente podríamos almacenarlos en un arreglo,
# pero no hemos llegado ahí, así que NO LO HAGAS ASÍ, debes pedir los números y almacenarlos en variables diferentes),
# de los 5 números ingresados, muestra cuántos fueron mayores que 10.


num1 = int(input("Ingresa un número: "))
num2 = int(input("Ingresa otro número: "))
num3 = int(input("Ingresa otro número: "))
num4 = int(input("Ingresa otro número: "))
num5 = int(input("Ingresa otro número: "))

contadorMayora10 = 0


if num1 > 10:
        contadorMayora10 += 1
if num2 > 10:
        contadorMayora10 += 1
if num3 > 10:
        contadorMayora10 += 1
if num4 > 10:
        contadorMayora10 += 1
if num5 > 10:
        contadorMayora10 += 1

print(f"Los números mayores a 10 fueron: {contadorMayora10}")