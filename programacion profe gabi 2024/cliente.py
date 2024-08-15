 #El cliente desea ingresar el nombre de un producto para la busqueda del mismo en la lista de stock productos y necesita que el programa le indique si el producto está en la lista de stock de productos o no  y sino debera mostrar un mensaje informando la ausencia del mismo en la lista de stock de productos
 listadeproductos=["chocolate", "ciruela"]
 buscar="chocolate"
if buscar in listadeproductos: 
    print ("chocolate se encuentra en la lista de productos")
else:
    print ("chocolate no se encuentra en la lista de productos")