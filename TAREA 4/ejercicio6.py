# Crea un diccionario con clave y valor producto : precio.
# Luego, pide una lista de productos comprados y muestra el total de la compra.
# Si el producto no existe, muestra una advertencia.

productos = {
    "manzana": 10,
    "pan": 15,
    "leche": 20,
    "huevo": 5,
    "cafe": 40,
    "cereal": 65,
    "azucar": 20
}

lista = input("Ingresa los productos comprados separados por comas: ")

comprados = [p.strip() for p in lista.split(",")]

total = 0

for producto in comprados:
    if producto in productos:
        total += productos[producto]
    else:
        print("Producto no disponible:", producto)

print("Total a pagar:", total)