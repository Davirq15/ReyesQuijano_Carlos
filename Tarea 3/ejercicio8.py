# Pide dos números y muestra todos los números entre ellos que sean múltiplos de 7.

num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

if num1 > num2:
    num1, num2 = num2, num1

print("Los números múltiplos de 7 entre", num1, "y", num2, ":")

for num in range(num1, num2 + 1):
    if num % 7 == 0:
        print(num)