#Haz un programa en Python que pida un número y muestre si está entre 10 y 20 (solo mostrando True o False).

numero = float(input("Introduce un número: "))

resultado = 10 < numero < 20
print(f"¿El número se encuentra entre el 10 y 20? {resultado}")