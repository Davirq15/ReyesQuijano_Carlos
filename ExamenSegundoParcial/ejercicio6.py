# Pide al usuario ingresar 10 productos y almacenalos en una lista. Luego muestra la lista ordenada alfabéticamente.

productos = []

for i in range(10):
    producto = input("Escribe el nombre de un producto: ")
    productos.append(producto)
productos.sort()
print("Lista de productos ordenada alfabéticamente:")
for producto in productos:
    print(producto)