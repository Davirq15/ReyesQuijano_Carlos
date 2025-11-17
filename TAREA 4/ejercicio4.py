# Haz un programa que pida un texto y una palabra. Si la palabra está en el texto, muestra cuántas veces aparece.

texto = input("Ingresa un texto: ")
palabra = input("Ingresa la palabra que desea buscar: ")

palabras = texto.split()
contador = palabras.count(palabra)

print("La palabra", palabra, "aparece", contador, "veces")