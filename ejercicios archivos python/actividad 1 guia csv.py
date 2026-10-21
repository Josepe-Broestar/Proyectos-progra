import csv

with open("empleados.csv", "a", encoding="utf-8", newline="") as empleados:
    escritor = csv.writer(empleados, delimiter=";")
    while True: 
        nombreempleado= input("Ingrese el nombre del empleado: ")
        cargo= input("Ingrese el cargo del empleado: ")
        sueldo= input("Ingrese el sueldo del empleado: ")
        confirmacion= input("Desea añadir otro empleado? (enter para si, n para no)")
        escritor.writerow([nombreempleado, cargo, sueldo])
        if confirmacion == "n":
            break
with open("empleados.csv", "r", encoding="utf-8") as empleadoslectura:
    lector = csv.reader(empleadoslectura, delimiter=";")
    next(lector)
    print("------------------------------------")
    for fila in lector:
        nombre, cargo, sueldo = fila
        print(f"{nombre} trabaja como {cargo} y gana {sueldo} pesos.")
    print("------------------------------------")
        
