prod=[]
rta="si"
while rta=="si" or rta=="Si" or rta=="SI":
    opcion=input("seleccione una opcion de la lista: 1. agregar un producto a la lista/n2. mostrar productos de la lista/n3. salir:      ")
    if opcion=="1":
        productoagregar= input ("ingrese el producto a agregar")
        prod.append (productoagregar)
    elif opcion=="2":
        print ("los productos de la lista son:/n________________________________")
        for p in prod:
            print(p,"/n___________________")
    elif opcion=="3":
        rta=input("esta seguro de salir del sistema:(si/no)")
        if rta=="no" or rta=="No" or rta=="NO":
            print("saliendo del sistema")
    else:
        print ("opcion invalida")    