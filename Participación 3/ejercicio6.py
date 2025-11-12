# Haz un programa que pida "Nombre" y "Calificaciones".
# Posteriormente calcula el promedio general, calificación mayor, calificación menor
# y muestra el nombre del mejor alumno.

nom = {}
total_calificaciones = 0

while True:
    nombre = input("Ecribe un nombre (Escribe *Salir* para salir): ")
    if nombre.lower() == "salir":
        break
    calificacion = float(input(f"Ingrese la calificación de {nombre}: "))
    nom[nombre] = calificacion
    total_calificaciones += calificacion
cantidad_nombres = len(nom)
promedio = total_calificaciones / cantidad_nombres if cantidad_nombres > 0 else 0
if nom:
    calificacion_mayor = max(nom.values())
    calificacion_menor = min(nom.values())
    mejor_alumno = [nombre for nombre, cal in nom.items() if cal == calificacion_mayor]
    print(f"Promedio general: {promedio:.2f}")
    print(f"Calificación mayor: {calificacion_mayor} del alumno(s): {', '.join(mejor_alumno)}")
    print(f"Calificación menor: {calificacion_menor}")
else:
    print("No se escribieron alumnos.")