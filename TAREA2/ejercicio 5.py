#Haz un programa en Python que pida un precio y muestre el total con IVA del 16%.

precio = float(input("Introduce el precio del producto: "))
iva = 0.16

precioConIVA = precio + (precio * iva)

print(f"El precio del producto con IVA es: {precioConIVA:.2f}")