# Pide nombres hasta que el usuario escriba la palabra "Fin".
# Al final muestra cuantos nombres ingresó, y cuál es el primero y el último.

nom = []

while True:
    nombre = input("Ingrese un nombre (Escribe *Fin* para salir): ")
    if nombre.lower() == "fin":
        break
    nom.append(nombre)

if nom:
    print(f"Cantidad de nombres escritoa: {len(nom)}")
    print(f"Primer nombre escrito: {nom[0]}")
    print(f"Último nombre escrito: {nom[-1]}")