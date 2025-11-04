# Haz un programa que pida un número, y calcule la suma de todos los números, desde el 1 hasta ese número.
# Por ejemplo, si ingresas 5, deberás sumar 1 + 2 + 3 + 4 +5.

num = int(input("Ingresa un número: "))
sumaT = 0

for i in range(1, num + 1):
    sumaT += i
print(f"El total de la suma de todos los números desde el 1 hasta {num} es de: {sumaT}")