# 10. Haz un programa que simule una calculadora básica con opciones de suma, resta, multiplicación y división,
# que se repita hasta que el usuario elija salir.

opcion = 0

while opcion != 5:
    print("Calculadora beta 1.0")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    opcion = int(input("Elige una opción: "))

    if opcion >= 1 and opcion <= 4:
        num1 = float(input("Escribe el primer número: "))
        num2 = float(input("Escribe el segundo número: "))

        if opcion == 1:
            print("Resultado: ", num1 + num2)
        elif opcion == 2:
            print("Resultado: ", num1 - num2)
        elif opcion == 3:
            print("Resultado: ", num1* num2)
        elif opcion == 4:
            if num2 != 0:
                print("Resultado: ", num1 / num2)
            else:
                print("Error: No se puede dividir entre cero.")
    elif opcion == 5:
        print("Saliendo...")
    else:
        print("Opción no existente. Intenta nuevamente.")