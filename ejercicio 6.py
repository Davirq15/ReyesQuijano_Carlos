#Haz un programa en Python que pida tres números y muestre si se cumple la expresión A < B < C (solo mostrando el resultado lógico).

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
num3 = float(input("Introduce el tercer número: "))

resultadoLogico = num1 < num2 < num3
print(f"¿Se cumple la expresión A < B < C? {resultadoLogico}")