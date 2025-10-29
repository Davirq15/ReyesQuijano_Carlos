#Haz un programa en Python que pida tres calificaciones y calcule su promedio con dos decimales.
#(Investiga la función round() en Python).

cal1 = float(input("Introduce la primera calificación: "))
cal2 = float(input("Introduce la segunda calificación: "))
cal3 = float(input("Introduce la tercera calificación: "))

promedio = round((cal1 + cal2 + cal3) / 3, 2)   #la función round() redondea el resultado a 2 decimales
print(f"El promedio de las calificaciones es: {promedio}")