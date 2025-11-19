# Haz un prograama que pida al usuario solicitar 5 calificaciones, soloacepta número del 1 al 10 (Si se permite decimales).
# Almacena estas 5 calificaciones en un arreglo, y posteriormente calcula el promedio de las calificaciones, muestra solamente 2 decimales.
# Si el alumno tiene una calificacion promedio mayor que 6, imprime un mensaje de "Aprobado", si tiene una calificacion menor que 6,
# imprimme "Reprobado", y si tiene una calificacion de 10, imprime "Exelente".

calificaciones = []

for i in range(5):
    calificacion = float(input("Ingresa una calificacion entre 1 y 10: "))
    while(calificacion < 1 or calificacion > 10):
        calificacion = float(input("Calificacion invalida. Ingresa una calificacion entre 1 y 10: "))
    calificaciones.append(calificacion)
promedio = sum(calificaciones) / len(calificaciones)
print(f"El promedio de las calificaciones es: {promedio:.2f}")
if promedio > 6 and promedio < 10:
    print("Aprobado")
elif promedio < 6:
    print("Reprobado")
else:
    print("Exelente")
