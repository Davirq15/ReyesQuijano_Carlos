# Haz un programa que pida un número, y muestre si es primo o no.

num = int(input("Ingresa un número: "))

if num <= 1:
    print(f"El número {num} no es primo.")
else:
    es_primo = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        print(f"El número {num} es primo.")
    else:
        print(f"El número {num} no es primo.")