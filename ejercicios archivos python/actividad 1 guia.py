import locale
from datetime import datetime

locale.setlocale(locale.LC_TIME, "es_CL.UTF-8")

ahora = datetime.now()
fecha = ahora.strftime("%A, %d de %B del %Y a las %H:%M")

with open("diario.txt", "a") as diario:
    entrada = input("¿Cómo te sientes?\n")
    diario.write(fecha)
    diario.write("\n")
    diario.write("\n")
    diario.write(entrada)
    diario.write("\n")
    diario.write("\n")
    diario.write("\n")
    