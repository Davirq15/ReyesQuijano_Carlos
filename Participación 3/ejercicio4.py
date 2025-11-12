# Pide una frase y cuenta cuántas vocales usa (a, e, i, o, u).

frase = input("Ingresa tu frase: ")
vocales = "aeiouAEIOU"
contador = 0
for char in frase:
    if char in vocales:
        contador += 1
print(f"La cantidad de vocales en esta frase es: {contador}")
