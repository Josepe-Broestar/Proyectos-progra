import csv
with open("compras.csv", "a", encoding="utf-8", newline="") as compras:
    escritor = csv.writer(compras, delimiter=";")
    
    while True:
        producto = input("Ingrese el nombre del producto: ")
        precio = input("Ingrese el precio del producto: ")
        escritor.writerow([producto, precio])
        confirmacion = input("Desea añadir otro producto? (enter para si, ´salir´ para salir) ")
        
        if confirmacion == "salir":
            break
with open("compras.csv", "r", encoding="utf-8", newline="") as compraslectura:
    lector = csv.reader(compraslectura, delimiter=";")
    next(lector)
    for fila in lector:
        producto, precio = fila
        print(f"{producto} cuesta {precio} pesos.")