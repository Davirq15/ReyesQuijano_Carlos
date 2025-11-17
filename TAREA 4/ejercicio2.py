# Haz un programa que pida una frase y cuenta cuántas veces aparece cada palabra.
# Por ejemplo "Esta es una prueba", "Esta" aparece una vez, "es", una vez, "una", una vez, etc...

frase = input("Escribe tu frase: ")

palabras = frase.split()
cont = {}

for palabra in palabras:
    if palabra in cont:
        cont[palabra] += 1
    else:
        cont[palabra] = 1

print(cont)