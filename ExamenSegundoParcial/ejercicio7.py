# Haz un programa que pida un número y determina si es par o impar.

num = int(input("Ingresa un número: "))

if num % 2 == 0:
    print(f"El número {num} es par.")
else:
    print(f"El número {num} es impar.")