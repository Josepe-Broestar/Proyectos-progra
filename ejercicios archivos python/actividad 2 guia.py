lineas = 0
caracteres = 0
palabras = 0
with open("texto.txt", "r") as texto:
    for linea in texto:
        lineas += 1
        palabras +=len(linea.split())
        for caracter in linea:
            caracteres += 1
    print("el texto tiene", lineas, "lineas")
    print(caracteres, "caracteres")
    print("y", palabras, "palabras")
    