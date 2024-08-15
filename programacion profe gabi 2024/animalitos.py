animales = ("canguro", "perro", "cocodrilo", "gato")
buscar=input("ingrese el elemento que desea buscar dentro de su tupla: ")
if buscar in animales:
    print ("el elemento", buscar, "se encuentra dentro de la tupla")
else:
    print ("el elemento", buscar, "no se encuentra dentro de la tupla")