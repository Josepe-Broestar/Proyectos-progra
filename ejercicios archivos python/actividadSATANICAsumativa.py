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

#PRODUCTOCONMASINGRESOS LISTO

def TotalVentasDelMes(mes, año, items, productos, ventas):
    total_mes = 0
    num_boleta = []
    with open(ventas, "r", encoding="utf-8") as ventas_archivo:
        lector = csv.reader(ventas_archivo, delimiter=";")
        for linea in lector:
            partes_fecha = linea[1].split("-")
            mes_searching = partes_fecha[1]
            año_searching = partes_fecha[2]
            if int(mes_searching) == int(mes) and int(año_searching) == int(año):
                num_boleta.append(linea[0])
    producto_vendido = {}
    with open(items, "r", encoding="utf-8") as items_archivo:
        lector_items = csv.reader(items_archivo, delimiter=";")
        for linea in lector_items:
            if linea[0] in num_boleta:
                id_producto = linea[1]
                cantidad = int(linea[2])
                if id_producto in producto_vendido:
                    producto_vendido[id_producto] += cantidad
                else:
                    producto_vendido[id_producto] = cantidad
    # Finalmente buscamos los precios y calculamos los ingresos
    with open(productos, "r", encoding="utf-8") as productos_archivo:
        lector_productos = csv.reader(productos_archivo)
        for linea in lector_productos:
            id_producto_archivo = linea[0]
            if id_producto_archivo in producto_vendido:
                precio = int(linea[2])
                cantidad = producto_vendido[id_producto_archivo]
                venta_producto = precio * cantidad
                total_mes += venta_producto
    return total_mes

totalmes = TotalVentasDelMes("10", "2010", "items.csv", "productos.csv", "ventas.csv")
print(totalmes)
#ohsi viejo

with open("informe.txt", "w", encoding="utf-8") as informe:
    informe.write(f"El producto más caro es {caro}\nEl valor total de la bodega es de ${total}\nEl producto con más ingresos es {productinho}\nEn el periodo de 10/2010, el total de ventas es ${totalmes}\n")