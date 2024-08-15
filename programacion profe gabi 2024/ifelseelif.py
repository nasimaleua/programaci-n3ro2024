n= int(input("ingrese algun numero:  "))
if n==10:
  print ("el numero es igual a 10")
elif n<10:
    print ("el numero es una unidad")
elif n<1000 and n>99:
    print ("el numero es una centena")
elif n<10000 and n>999:
    print ("el numero es una milena")
else:
   print ("el numero es una decena o centena")
