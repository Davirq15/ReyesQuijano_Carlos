# Haz un programa que genera la tabla de multiplicar de un número ingresado.
# Al final, muestra cuantos resultados de las multiplicaciones fueron mayores que 50,
# cuántos menores que 50 y cuántos iguales a 50.

num = int(input("Ingresa un número:"))
mayora50 = 0
menora50 = 0
iguala50 = 0

for i in range(1, 11):
    resultado = num * i
    print(f"{num} x {i} = {resultado}")
    if resultado > 50:
        mayora50 += 1
    elif resultado < 50:
        menora50 += 1
    else:
        iguala50 += 1
print(f"Números mayores a 50: {mayora50}")
print(f"Números menores a 50: {menora50}")
print(f"Números iguales a 50: {iguala50}")