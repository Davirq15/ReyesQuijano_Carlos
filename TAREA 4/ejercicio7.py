# Haz un programa en Python que pida repetidamente el nombre de una persona y su respuesta ("Si" o "No").
# Guarda cada respuesta en un diccionario, donde la clave sea el nombre y el valor la respuesta.
# El programa debe terminar cuando el usuario escriba "Fin" como nombre.
# Al finalizar, muestra cuántas personas respondieron "Si", y cuántas respondieron "No"

resultados = {}

while True:
    nombre = input("Nombre (o escribe 'Fin' para terminar): ")
    if nombre.lower() == "fin":
        break
    
    respuesta = input("Respuesta (Si / No): ")
    resultados[nombre] = respuesta

si_count = 0
no_count = 0

for r in resultados.values():
    if r.lower() == "si":
        si_count += 1
    elif r.lower() == "no":
        no_count += 1

print("Personas que respondieron con 'Si':", si_count)
print("Personas que respondieron con 'No':", no_count)