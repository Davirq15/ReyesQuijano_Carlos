# # Pide una frase, divídela en palabras y guarda una lista solo las que tengan más de 5 letras.
# # Muestra la lista resultante.

frase = input("Escribe alguna frase: ")

palabras = frase.split()

resultado = [palabra for palabra in palabras if len(palabra) > 5]

print("Palabras de más de 5 letras:")
print(resultado)
