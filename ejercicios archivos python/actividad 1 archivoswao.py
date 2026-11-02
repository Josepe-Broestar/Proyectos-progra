import csv
#with open("notas.txt", "r+") as notasnocsv:
 #   contenido = notasnocsv.read()
 #   encabezado = csv.writer(notasnocsv, delimiter = ":")
   # if not contenido.startswith("nombre"):
     #   encabezado.writerow("nombre:nota1:nota2:nota3:nota4:nota5:nota6\n")
with open("notas.txt", "r+") as notascsv:
    lector = csv.reader(notascsv, delimiter=":")
    for fila in lector:
        nombre = fila[0]
        # notas = float(fila[1:6])
        notas = []
        for n in fila[1:6]:
            notas.append(float(n))
        if sum(notas)/6 < 4.0:
            print(f"{nombre} ha reprobado")
        else:
            print(f"{nombre} ha aprobado")
        
        
        