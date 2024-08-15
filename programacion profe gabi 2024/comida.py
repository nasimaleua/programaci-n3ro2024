listadiafrio= ["sopa de tomate","guiso de lenteja","sopa de albondigas"]
listadiacalor= ["bife","papas al horno","ensalada"]
clima=int(input("ingrese temperatura: "))
if clima>25 or clima<40:
    print ("comidas para este temperatura: ",listadiacalor)
else:
    print ("comidas para este temperatura:  ", listadiafrio)