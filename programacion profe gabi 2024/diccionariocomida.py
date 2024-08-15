recetas={"hamburguesa":{"pan de hamburguesa":1,"Swits":1,"huevo frito":1,}}
print (recetas)
for t, v in recetas.items():
    print (t,":",v)
    print (f"(c):(v)")
    if "hamburguesas" in v:
        print ("la receta existe y tiene clave:",t)