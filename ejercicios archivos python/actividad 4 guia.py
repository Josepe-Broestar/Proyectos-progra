with open ("estudiantes.txt", "a", encoding="utf-8") as estudiantes:
    while True:
        nombreapellido= input("ingrese el nombre y apellido de(la) estudiante: ")
        nota= input("ingrese la nota de(la)estudiante: ")
        estudiantes.write(nombreapellido + "-" + nota)
        estudiantes.write("\n")
        confirmacion= input("desea seguir escribiendo? (enter para si, n para no)")
        if confirmacion.lower == "n":
            break
        