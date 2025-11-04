# Pide una cantidad de productos y su precio uno por uno, luego muestra el total con IVA del 16%.

cantidadP = int(input("Ingresa la cantidad total de productos: "))
total = 0.0

for i in range(cantidadP):
    precio = float(input(f"Escribe el precio del producto {i + 1}: "))
    total += precio
iva = total * 0.16
total_con_iva = total + iva
print(f"El total con IVA del 16% es: {total_con_iva:.2f}")