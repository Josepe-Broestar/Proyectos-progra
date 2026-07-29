def espalindromo(palabra):
    palabra_limpia = palabra.lower()
    if palabra_limpia == palabra_limpia[::-1]:
        return(f"{palabra} es un palindromo")
    else:
               return(f"{palabra} no es un palindromo")
print(espalindromo("paralelepipedo"))