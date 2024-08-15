provincias={ "buenos aires": "la plata","catamarca":"san fernando del valle de catamarca","chaco":"resistencia","chubut":"rawson","cordoba":"ciudad de cordoba","corrientes":"ciudaded de corrientes","entre rios":"paraná","formosa":"formosa","jujuy":"san salvador dec jujuy","la pampa":"ciudad de santa rosa","la rioja":"la rioja","mendoza":"mendoza","misiones":"posadas","neuquen":"neuquen","rio negro":"viedma","salta":"salta","san juan":"ciudad de san juan","san luis":"ciudad de san luis","santa cruz":"rio gallegos","santa fe":"ciudad de santa fe","santiago de estero":"ciudad de santiago del estero","ushuaia":"tierra del fuego","tucuman":"san miguel de tucuman"}


pciaBuscarValorCapital=input("Ingresar provincia a buscar capital: ")
#Buscamos el valor por clave, en este caso capital ingresando provincia
x = provincias[pciaBuscarValorCapital]
print("su capital es:",x)
print("_______________________")




for p, c in provincias.items():
    print(p, "-", c)
