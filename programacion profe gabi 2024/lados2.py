lados= int(input("ingrese el numero de lados:  "))
r=str
if lados==4:
   r= (input("sus cuatro lados son iguales?  "))
if r=="si":
  print ("es un cuadrado")
elif r=="no":
  print ("es un rectangulo o un paralelogramo")
elif lados==3:
  print ("es un triangulo")