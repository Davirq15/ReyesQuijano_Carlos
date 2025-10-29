#Haz un programa en Python que convierta una cantidad de minutos a horas.


minutos = int(input("Ingresa los minutos: "))

conversionAHoras = round(minutos / 60)  #redondea el resultado a horas completas

print(f"El total en horas de {minutos} minutos es: {conversionAHoras} horas")