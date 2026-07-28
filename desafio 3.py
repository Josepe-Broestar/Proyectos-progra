mensaje = input("Ingrese el mensaje en codigo: ")
traduccion = ""

codigo = {
    "@": "A",
    "#": "E",
    "&": "I",
    "$": "O",
    "*": "U",
    "%": "M",
    "+": "N",
    "!": "R",
    "?": "S",
    "=": "T"
}

for caracter in mensaje:
    if caracter in codigo:
        traduccion += codigo[caracter]
    else:
        traduccion += caracter

print("Mensaje traducido:", traduccion)
# usar esto de ejemplo: H$l@ M*+D$
# para no tener que escribirlo a mano :D