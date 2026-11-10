import csv
def ProductoMasCaro(productos):
    with open(productos, "r", encoding="utf-8") as productos_archivo:
        lector = csv.reader(productos_archivo)
        mayor = 0
        nombre_mayor = None
        for fila in lector:
            actual = int(fila[2])
            if actual > mayor:
                mayor = actual
                nombre_mayor = fila[1]
        return nombre_mayor
caro = ProductoMasCaro("productos.csv")

#PRODUCTO MAS CARO LISTO
def ValorTotalBodega(productos):
    with open(productos, "r", encoding="utf-8") as productos_archivo:
        lector = csv.reader(productos_archivo)
        valor_total = 0
        for fila in lector:
            valor_total += int(fila[2]) * int(fila[3])
    return valor_total
total = ValorTotalBodega("productos.csv")

#VALOR TOTAL LISTO

def ProductoConMasIngresos(items, productos):
    ventas = {}

    with open(items, "r", encoding="utf-8") as items_archivo:
        lector = csv.reader(items_archivo, delimiter=";")
        for fila in lector:
            id_prod = fila[1]
            cantidad = int(fila[2])
            if id_prod in ventas:
                ventas[id_prod] += cantidad
            else:
                ventas[id_prod] = cantidad
    precios = {}

    with open(productos, "r", encoding="utf-8") as productos_archivo:
        lector = csv.reader(productos_archivo)
        nombres = {}
        for fila in lector:
            id_prod = fila[0]
            precio = int(fila[2])
            precios[id_prod] = precio
            nombres[fila[0]] = fila[1]
    ventas_total = {}
    for id_producto in ventas:
        nombres
        cantidad = ventas[id_producto]
        precio = precios[id_producto]
        ventas_total[id_producto] = cantidad * precio
    idpro = max(ventas_total, key=ventas_total.get)

    return nombres[idpro]

productinho = ProductoConMasIngresos("items.csv", "productos.csv")
print(productinho)
            