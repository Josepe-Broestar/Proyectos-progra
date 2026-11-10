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
print(caro)
#PRODUCTO MAS CARO LISTO
def ValorTotalBodega(productos):
    with open(productos, "r", encoding="utf-8") as productos_archivo:
        lector = csv.reader(productos_archivo)
        valor_total = 0
        for fila in lector:
            valor_total += int(fila[2]) * int(fila[3])
    return valor_total
total = ValorTotalBodega("productos.csv")
print(total)
#VALOR TOTAL LISTO
def ProductoConMasIngresos(items, productos):
    producto = {}
    with open(items, "r", encoding="utf-8") as items_archivo:
        lector = csv.reader(items_archivo)
        for fila in lector:
            id_prod = fila[1]
            cantidad = int(fila[2])
            if id_prod in ventas_totales:
                producto[id_prod] += cantidad
            else:
                producto[id_prod] = cantidad
        with open(productos, "r", encoding="utf-8") as productos_archivo:
            lector = csv.reader(productos_archivo)
            precios= {}
            for fila in lector:
                id_prodV = fila[0]
                precio = int(fila[2])
                if id_prod in ventas_totales:
                    producto[id_prod] += precio
                else:
                    producto[id_prod] = precio
            
                    
                    
    return max(producto, key=producto.get)
 
            