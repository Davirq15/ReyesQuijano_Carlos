# Haz un programa que sume todos los números pares del 1 al 100. Al final muestra el resultado de la suma.

sumaPares = 0
Inicio = input("Presiona Enter para iniciar la suma de los números!!")

for i in range(1, 101):
    if i % 2 == 0:
        sumaPares += i
print(f"El total de la suma de los números pares del 1 al 100 es: {sumaPares}")