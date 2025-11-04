# Haz un programa que sume todos los números impares del 1 al 50.

sumaI = 0
Inicio = input("Presiona Enter para iniciar la suma...")

for i in range(1, 51):
    if i % 2 != 0:
        sumaI += i
print(f"El total de la suma de los números impares del 1 al 50 es: {sumaI}")