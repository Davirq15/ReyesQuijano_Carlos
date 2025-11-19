# Haz un prograama que pida una palabra, y cuenta cuants vocales tiene la palabra ingresada.

palabra = input("Escriba alguna palabra: ")
vocales = "aeiouAEIOU"
contadordeVocales = 0

for letra in palabra:
    if letra in vocales:
        contadordeVocales += 1
print(f"La palabra {palabra} tiene {contadordeVocales} vocales.")