frase = input("ingrese una frase u oracion: ")
vocales = "aeiouAEIOU"
cantidadvocales = 0

for vocal in (frase):
    if vocal in vocales:
        cantidadvocales += 1
        
print("la frase tiene", cantidadvocales, "vocales.")