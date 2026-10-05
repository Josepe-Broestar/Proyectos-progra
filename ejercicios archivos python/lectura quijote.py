archivo = open("C:/Users/Alumno_001/Desktop/PROGRA2026/Proyectos-progra/PBD/quijote.txt.txt", "r")
for linea in archivo:
    print(linea)
    
archivo.close()

archivo = open("C:/Users/Alumno_001/Desktop/PROGRA2026/Proyectos-progra/PBD/quijote.txt.txt", "a")
archivo.write("\nde los de lanza en astillero")
archivo.close()