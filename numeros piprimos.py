cantidad = int(input("ingrese cantidad de numeros primos que desee calcular: "))
numero = 1
esprimo = True
primo = 0
divisiones = 0
divisores = 0
for i in range(cantidad):
    numero += 1
    esprimo = True
    divisores = 0
    divisiones = 0
    while esprimo == True:
        divisiones +=1
        if numero % divisiones == 0:
            divisores += 1
        if divisiones == numero:
            print (numero, "es primo")
            break
        if divisores > 2:
            esprimo = False
        


