# Haz un programa que pida el nombre de un contacto y su teléfono, y los agregue a un diccionario.

contactos = {}

nombre = input("Nombre: ")
telefono = input("Teléfono (con prefijo telefónico): ")

contactos[nombre] = telefono

print("Contacto guardado:", contactos)