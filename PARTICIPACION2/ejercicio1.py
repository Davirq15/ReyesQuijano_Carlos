# Haz un programa en Python que pida un número, posteriormente muestra todos los números desde 1 hasta el número ingresando.
# Imprime en consola un coteo de números pares y de números impares.

num = int(input("Ingresa un número: "))
contadorPar = 0
contadorImpar = 0

for i in range(1, num + 1):

    if i % 2 == 0:
         contadorPar += 1
    
    else:
         contadorImpar += 1
    print(i)

print(f"Números que son pares: {contadorPar}")
print(f"Números que son impares: {contadorImpar}")