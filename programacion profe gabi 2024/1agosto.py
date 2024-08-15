rta="si"
       #rta!="no":
while rta=="si":
    opcion=input("Menú de opciones\n1-Saludo\n2-Despedida\n3-salir\n")
           
    if opcion=="3":
       rta=input(" Desea consultar otra opción de menú? si/no:")
         
           








______________________________________
while True:#condición a evaluar
    opcion=input("Menú de opciones\n1-Saludo\n2-Despedida\n3-salir\n")
    if opcion=="1":
        print("Hola")  
    elif opcion=="2":
        print("Chau")        
    elif opcion=="3":
        print("Saliendo del sistema")
        break
    else:
        print("La opción ingresada es invalida")    
   
