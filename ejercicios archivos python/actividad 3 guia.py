cortapapeles = ""

with open("origen.txt", "r", encoding="utf-8") as original:
    for linea in original:
        cortapapeles += linea
        
with open("copia.txt", "a", encoding="utf-8") as copia:
    copia.write(cortapapeles)
    copia.write("\n")