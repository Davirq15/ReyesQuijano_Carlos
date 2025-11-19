# Haz un programaque pida una frase y cuenta cuantas letras tiene la frase, sin contar espacios.

frase = input("Escribe alguna frase: ")

fraseSinEspacios = frase.replace(" ", "")
cantidadLetras = len(fraseSinEspacios)

print(f"Esta frase tiene {cantidadLetras} letras, sin estar contando espacios.")