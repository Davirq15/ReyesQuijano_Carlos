#Haz un progrema que pida una cantidad y la convierta de grados Celsius a Fahrenheit.

celsius = float(input("Ingrese la cantidad de grados celsius ahora: "))
fahrenheit = (celsius * 9/5) + 32

print(f"{celsius} grados Celsius son ahora {fahrenheit} grados Fahrenheit")