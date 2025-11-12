# Pide números hasta que el usuario escriba 0.
# Guarda los pares en una lista y los impares en otra. 
# Al final, muestra cuantos números hay en cada lista.
# Ordena la lista en orden ascendente y recorre las listas para mostrar cada número uno por uno.

par = []
impar = []



while True:
    numero = int(input("Escribe un número (Escribe *0* para finalizar): "))
    if numero == 0:
        break
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)
par.sort()
impar.sort()
print(f"Cantidad de números par: {len(par)}")
print(f"Cantidad de números impar: {len(impar)}")
print("Números par:")
for num in par:
    print(num)
print("Números impar:")
for num in impar:
    print(num)