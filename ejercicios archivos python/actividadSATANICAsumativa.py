import csv                                                  
def ProductoMasCaro(productos):                             
        with open(productos, "r", encoding="utf-8") as productos_archivo: 
            lector = csv.reader(productos_archivo)          
            mayor = 0                                       # Inicializa variable para guardar el precio máximo encontrado
            nombre_mayor = None                             # Inicializa la variable para almacenar el nombre del producto
            for fila in lector:                             # Itera a través de cada fila del archivo
                actual = int(fila[2])                       # Extrae el precio de la fila y lo convierte a entero
                if actual > mayor:                          # Compara si el precio actual supera al mayor registrado
                    mayor = actual                          # Actualiza el precio máximo
                    nombre_mayor = fila[1]                  # Guarda el nombre correspondiente al producto más caro
            return nombre_mayor                             # Retorna el nombre del producto más caro al finalizar
caro = ProductoMasCaro("productos.csv")                     

#PRODUCTO MAS CARO LISTO

def ValorTotalBodega(productos):                           
        with open(productos, "r", encoding="utf-8") as productos_archivo: 
            lector = csv.reader(productos_archivo)          # Inicializa el lector de CSV
            valor_total = 0                                 # Acumulador para el valor total en dinero de la bodega
            for fila in lector:                             # Recorre cada producto en el archivo
                valor_total += int(fila[2]) * int(fila[3])  # Multiplica precio por stock y lo acumula al total
        return valor_total                                  # Retorna la suma total calculada
total = ValorTotalBodega("productos.csv")                   

#VALOR TOTAL LISTO

def ProductoConMasIngresos(items, productos):               
        ventas = {}                                         # Diccionario para sumar cantidades vendidas por ID de producto

        with open(items, "r", encoding="utf-8") as items_archivo: 
            lector = csv.reader(items_archivo, delimiter=";") 
            for fila in lector:                             # Recorre cada línea de ítems vendidos
                id_prod = fila[1]                           # Extrae el identificador del producto
                cantidad = int(fila[2])                     # Extrae la cantidad vendida en esa línea
                if id_prod in ventas:                       # Verifica si el ID ya fue registrado antes
                    ventas[id_prod] += cantidad             # Suma la cantidad si ya existe en el diccionario
                else:                                       # Si es la primera vez que aparece el producto
                    ventas[id_prod] = cantidad              # Lo inicializa con su cantidad vendida
        precios = {}                                        # Diccionario para almacenar los precios de los productos
        with open(productos, "r", encoding="utf-8") as productos_archivo: # Abre el catálogo de productos
            lector = csv.reader(productos_archivo)          # Crea el lector de CSV
            nombres = {}                                    # Diccionario para relacionar ID con nombre del producto
            for fila in lector:                             # Recorre cada producto del catálogo
                id_prod = fila[0]                           # Extrae el ID
                precio = int(fila[2])                       # Extrae el precio unitario
                precios[id_prod] = precio                   # Guarda el precio vinculado a su ID
                nombres[fila[0]] = fila[1]                  # Guarda el nombre vinculado a su ID
        ventas_total = {}                                   # Diccionario para almacenar los ingresos totales por producto
        for id_producto in ventas:                          # Recorre cada producto que tuvo ventas registradas
            nombres                                         # Referencia directa al diccionario de nombres (sin afectar ejecución)
            cantidad = ventas[id_producto]                  # Obtiene la cantidad total vendida del producto
            precio = precios[id_producto]                   # Obtiene el precio unitario del producto
            ventas_total[id_producto] = cantidad * precio   # Calcula ingresos multiplicando cantidad por precio unitario
        idpro = max(ventas_total, key=ventas_total.get)     # Busca la clave con el mayor valor de ingresos acumulados
        return nombres[idpro]                               # Retorna el nombre del producto con más ingresos

productinho = ProductoConMasIngresos("items.csv", "productos.csv")
print(productinho)                                      

#PRODUCTOCONMASINGRESOS LISTO

def TotalVentasDelMes(mes, año, items, productos, ventas): 
        total_mes = 0                                       # Acumulador del total de dinero recaudado en el mes
        num_boleta = []                                     # Lista para almacenar los IDs de boletas que cumplen con la fecha
        with open(ventas, "r", encoding="utf-8") as ventas_archivo: # Abre el registro general de ventas/boletas
            lector = csv.reader(ventas_archivo, delimiter=";") # Configura el lector delimitado por punto y coma
            for linea in lector:                            # Itera sobre cada registro de venta
                partes_fecha = linea[1].split("-")          # Divide la fecha en partes (día, mes, año) usando el guion
                mes_searching = partes_fecha[1]             # Extrae el mes de la transacción
                año_searching = partes_fecha[2]             # Extrae el año de la transacción
                if int(mes_searching) == int(mes) and int(año_searching) == int(año): # Filtra si coincide con el mes y año buscados
                    num_boleta.append(linea[0])               # Guarda la boleta válida en la lista
        producto_vendido = {}                               # Diccionario para sumar cantidades vendidas en ese periodo específico
        with open(items, "r", encoding="utf-8") as items_archivo: 
            lector_items = csv.reader(items_archivo, delimiter=";") 
            for linea in lector_items:                      # Recorre cada ítem asociado a las transacciones
                if linea[0] in num_boleta:                  # Comprueba si el ítem pertenece a una boleta del mes buscado
                    id_producto = linea[1]                  # Extrae el ID del producto vendido
                    cantidad = int(linea[2])                  # Extrae la cantidad vendida
                    if id_producto in producto_vendido:       # Verifica si ya se había registrado este producto en el mes
                        producto_vendido[id_producto] += cantidad # Suma la nueva cantidad al acumulador mensual del producto
                    else:                                   # Si es el primer registro del producto en este mes
                        producto_vendido[id_producto] = cantidad # Inicializa su cantidad en el diccionario
        with open(productos, "r", encoding="utf-8") as productos_archivo: 
            lector_productos = csv.reader(productos_archivo) 
            for linea in lector_productos:                  # Recorre cada producto disponible
                id_producto_archivo = linea[0]              # Extrae el ID del producto del catálogo
                if id_producto_archivo in producto_vendido: # Verifica si el producto tuvo ventas en el mes evaluado
                    precio = int(linea[2])                  # Obtiene el precio del producto
                    cantidad = producto_vendido[id_producto_archivo] # Obtiene la cantidad total vendida en el periodo
                    venta_producto = precio * cantidad      # Calcula el dinero generado por este producto (precio * cantidad)
                    total_mes += venta_producto             # Acumula los ingresos del producto al total general del mes
        return total_mes                                    # Retorna el total de ventas monetarias del mes calculado

totalmes = TotalVentasDelMes("10", "2010", "items.csv", "productos.csv", "ventas.csv")
print(totalmes)                                         


withopen("informe.txt", "w", encoding="utf-8") as informe:
    informe.write(f"El producto más caro es {caro}\nEl valor total de la bodega es de ${total}\nEl producto con más ingresos es {productinho}\nEn el periodo de 10/2010, el total de ventas es ${totalmes}\n") # Escribe el reporte completo con todos los resultados obtenidos