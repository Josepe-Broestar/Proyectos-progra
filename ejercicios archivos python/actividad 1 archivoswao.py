import csv
with open("notas.txt", "r+") as notasnocsv:
    contenido = notanocsv.read()
    encabezado = csv.writer(notasnocsv, delimeter = ":")
    if not contenido.startswith("nombre"):
        encabezado.writerow("nombre:nota1:nota2:nota3:nota4:nota5:nota6\n")
with open("notas.txt", "
        
        