#Haz un programa en Python que pida tres números y muestre si los tres son iguales (solo mostrando True o False).

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
num3 = float(input("Introduce el tercer número: "))

resultado = (num1 == num2 == num3)
print(f"¿Los tres números son iguales? {resultado}")