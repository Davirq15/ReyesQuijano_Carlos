#Haz un programa en Python que pida el radio y la altura de un cilindro y muestre su volumen.

radio = float(input("Introduce el radio del cilindro: "))
altura = float(input("Introduce la altura del cilindro: "))

volumenCilindro = 3.1416 * (radio ** 2) * altura  #se puede usar math.pi para mayor precisión
print(f"El volumen del cilindro es: {volumenCilindro:.2f}")