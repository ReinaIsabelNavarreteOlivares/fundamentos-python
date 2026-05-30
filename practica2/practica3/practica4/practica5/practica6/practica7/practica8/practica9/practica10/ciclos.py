#ciclo, iteración bucle

#while
i=0
while i < 10:
    if i < 5:
       print("El numero",i, "es menor a 5")
    else:
        print("el numero",i,"es mayor o igual a 5")

        i+1

        print("termino la iteración")

        #for x in range (1,11):
             #print(x)
    while True:
        print("escribe la opción deseada")
        print("1:saludar")
        print("2:salir")

    respuesta= int(input())
    if respuesta == 1:
        print("saludos terricola!")
    elif respuesta == 2:
        break
    print("terminando programa")

