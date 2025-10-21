#Haz un programa que solicite al usuario la base y la altura de un rectangulo,
# y calcula su area y perimetro.

base = float(input("Escribe la base del rectángulo: "))
altura = float(input("Escribe la altura del rectángulo: "))

area = base * altura
perimetro = 2 * (base + altura)
print(f"El área del rectángulo es: {area}")
print(f"El perímetro del rectángulo es: {perimetro}")