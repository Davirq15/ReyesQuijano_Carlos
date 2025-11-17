# Haz un programa que pida al usuario una contraseña.
# Verifica que: La contraseña tenga al menos 8 caracteres, y que contenga al menos una mayúscula y un número.

importante = input("Para crear una contraseña debe tener al menos 8 caracteres, y que contenga al menos una mayúscula y un número. (OPRIME ENTER)")
contraseña = input("Crea una contraseña: ")

tiene_mayuscula = False
tiene_numero = False

for caracter in contraseña:
    if caracter.isupper():
        tiene_mayuscula = True
    if caracter.isdigit():
        tiene_numero = True

if len(contraseña) >= 8 and tiene_mayuscula and tiene_numero:
    print("Contraseña válida")
else:
    print("Contraseña NO válida")