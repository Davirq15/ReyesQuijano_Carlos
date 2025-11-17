# Haz un programa que pida una palabra y verifique si inicia con una vocal.

palabra = input("Escribe una palabra: ")

vocales = "aeiouAEIOU"

if palabra and palabra[0] in vocales:
    print("La palabra SI inicia con una vocal")
else:
    print("La palabra NO inicia con una vocal")