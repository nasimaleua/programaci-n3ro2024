frutas = ("apple", "banana", "cherry", "apple")
buscar=input("ingrese el elemento que desea buscar dentro de su tupla")
if buscar in frutas:
    print ("el elemento", buscar, "se encuentra dentro de la tupla")
else:
    print ("el elemento", buscar, "no se encuentra dentro de la tupla")