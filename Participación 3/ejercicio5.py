# Haz un programa que pida un número, y crea una nueva lista sin duplicados.

num = []


while True:
    numero = int(input("Escribe un número (Escribe *0* para salirte): "))
    if numero == 0:
        break
    if numero not in num:
        num.append(numero)
print("Lista sin repetidos:")
for num in num:
    print(num)