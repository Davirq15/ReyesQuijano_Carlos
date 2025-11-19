# Haz un programa que pida un número entero N, y calcula la suma de todos los números del 1 al N.

N = int(input("Ingresa un número: "))
suma = 0

for i in range(1, N + 1):
    suma += i
print(f"La suma de todos los números apartir del 1 al {N} es: {suma}")