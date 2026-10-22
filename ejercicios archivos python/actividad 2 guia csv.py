import csv
promedio = 0
contador = 0
with open("estudiantes.csv", "r", encoding="utf-8") as estudiantes:
    lector = csv.reader(estudiantes)
    next(lector)
    for linea in lector:
        nota = float(linea[1])
        contador += 1
        promedio += nota
    print(promedio / contador)