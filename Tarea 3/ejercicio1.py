# Haz un programa que calcule cuántos números del 1 al 100 son divisibles entre 3 y entre 5.

contador = 0
inicio = input("Presiona Enter para iniciar el conteo...")

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        contador += 1
    
print(f"{contador}, Es el total de números del 1 al 100 que son divisibles entre 3 y entre 5. ")