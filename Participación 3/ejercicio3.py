# Haz un programa que pida "Nombre" y "Calificación".
# Almacena todos estos datos en un diccionario.
# Posteriormente muestra: Promedio general, cantidad de aprobados y cantidad de reprobados.

nom = {}
totalCalificaciones = 0


while True:
    nombre = input("Ecribe un nombre (Escribe *Fin* para salir): ")
    if nombre.lower() == "fin":
        break
    calificacion = float(input(f"Ingrese la calificación de {nombre}: "))
    nom[nombre] = calificacion
    total_calificaciones += calificacion
cantidad_nombres = len(nom)
promedio = total_calificaciones / cantidad_nombres if cantidad_nombres > 0 else 0
aprobados = sum(1 for cal in nom.values() if cal >= 60)
reprobados = cantidad_nombres - aprobados
print(f"Promedio general: {promedio:.2f}")
print(f"Cantidad de aprobados: {aprobados}")
print(f"Cantidad de reprobados: {reprobados}")
