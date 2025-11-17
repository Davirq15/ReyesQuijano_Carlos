# Pide al usuario una lista de palabras (separadas por comas, por ejemplo Hola, Mario, Python, Programación).
# Elimina los elementos repetidos y los que sean menores a 3 letras.
# Muestra la nueva lista e imprímela en pantalla. 

lista = input("Ingresa una lista de palabras que este separadas por comas: ")

palabras = [p.strip() for p in list.split(",")]

sin_repetidos = []
for p in palabras:
    if p not in sin_repetidos and len(p) >= 3:
        sin_repetidos.append(p)

print("Lista final:", sin_repetidos)