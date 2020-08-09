# Exercices

# Mostrar el precio del IVA de un producto con un valor de 100 y su precio final.

print("Para calcular el precio total (costo + % iva) de un producto necesitamos algunos datos, por favor:" "\n")
precio = int(input("Digite el costo del articulo : "))
iva = int(input ("porcentaje de iva: "))
total = ((precio + (precio * (iva/100))))
print("El precio a pagar es: ", str(total), "€")

# Crea una variable numérica y si esta entre 0 y 10, mostrar un mensaje indicándolo.
mynumber = int(input("Digite un número : "))
if (mynumber in (range(0,11))):
  print("esta entre 0 y 10: %d" % mynumber)
else:
  print("No esta entre 0 y 10: %d" % mynumber)

# Crea una variable numérica y si esta entre 0 y 10, mostrar un mensaje indicándolo, que si esta entre 11 y 20, muestre otro mensaje diferente y si esta entre 21 y 30 otro mensaje.

mynumber = int(input("Digite un número : "))
if (mynumber in (range(0,11))):
  print("El número %d esta entre 0 y 10" % mynumber)
elif (mynumber in (range(11,21))): # else if
  print("El número %d esta entre 11 y 20" % mynumber)
elif(mynumber in (range(21,31))): # else if
  print("El número %d esta entre 21 y 30" % mynumber)
else:
  print("El número %d No esta entre 0 y 30" % mynumber)


mynumber = int(input("Digite un número : "))
if(mynumber>=1 and mynumber<=10):
    print("Esta entre 1 y 10")
elif(mynumber>=11 and mynumber<=20):
    print("Esta entre 11 y 20")
elif(mynumber>=21 and mynumber<=30):
    print("Esta entre 21 y 30")
else:
    print("No esta en ese rango")

# Mostrar con un while los números del 1 al 100.    
mynumber=1
while(mynumber<=100):
    print(mynumber)
    mynumber +=1
print("Fin del while: %d" %mynumber)

# Mostrar con un for los números del 1 al 100.

for mynumber in range(1,101):
  print(mynumber)
print("Fin del for: %d" %mynumber)

# Mostrar los caracteres de la cadena “Hola mundo”.
for i in "Hola mundo":
    print(i)

mystring = "Hola mundo"
lon=int((len(mystring)))
print("%d: ", lon)
i=0
while(i<lon):
  print("%s: " %mystring[i])
  i += 1
print("Fin del while: %d: " %i)

#  Mostrar los números pares entre 1 al 100.
for i in range(1,101):
  if((i%2) == 0):
    print(i)
print("Fin del for: %d: " %i)

# Generar un rango entre 0 y 10
lst=[i for i in range(0,11)]
print("lst: " ,str(lst))

rango = list( range(10) )
print(rango)


# Exercices

# Mostrar el precio del IVA de un producto con un valor de 100 y su precio final.

print("Para calcular el precio total (costo + % iva) de un producto necesitamos algunos datos, por favor:" "\n")
precio = int(input("Digite el costo del articulo : "))
iva = int(input ("porcentaje de iva: "))
total = ((precio + (precio * (iva/100))))
print("El precio a pagar es: ", str(total), "€")

# Crea una variable numérica y si esta entre 0 y 10, mostrar un mensaje indicándolo.
mynumber = int(input("Digite un número : "))
if (mynumber in (range(0,11))):
  print("esta entre 0 y 10: %d" % mynumber)
else:
  print("No esta entre 0 y 10: %d" % mynumber)

# Crea una variable numérica y si esta entre 0 y 10, mostrar un mensaje indicándolo, que si esta entre 11 y 20, muestre otro mensaje diferente y si esta entre 21 y 30 otro mensaje.

mynumber = int(input("Digite un número : "))
if (mynumber in (range(0,11))):
  print("El número %d esta entre 0 y 10" % mynumber)
elif (mynumber in (range(11,21))): # else if
  print("El número %d esta entre 11 y 20" % mynumber)
elif(mynumber in (range(21,31))): # else if
  print("El número %d esta entre 21 y 30" % mynumber)
else:
  print("El número %d No esta entre 0 y 30" % mynumber)


mynumber = int(input("Digite un número : "))
if(mynumber>=1 and mynumber<=10):
    print("Esta entre 1 y 10")
elif(mynumber>=11 and mynumber<=20):
    print("Esta entre 11 y 20")
elif(mynumber>=21 and mynumber<=30):
    print("Esta entre 21 y 30")
else:
    print("No esta en ese rango")

# Mostrar con un while los números del 1 al 100.    
mynumber=1
while(mynumber<=100):
    print(mynumber)
    mynumber +=1
print("Fin del while: %d" %mynumber)

# Mostrar con un for los números del 1 al 100.

for mynumber in range(1,101):
  print(mynumber)
print("Fin del for: %d" %mynumber)

# Mostrar los caracteres de la cadena “Hola mundo”.

for i in "Hola mundo":
    print(i)

mystring = "Hola mundo"
lon=int((len(mystring)))
print("%d: ", lon)
i=0
while(i<lon):
  print("%s: " %mystring[i])
  i += 1
print("Fin del while: %d: " %i)

#  Mostrar los números pares entre 1 al 100.
for i in range(1,101):
  if((i%2) == 0):
    print(i)
print("Fin del for: %d: " %i)

# Generar un rango entre 0 y 10
lst=[i for i in range(0,11)]
print("lst: " ,str(lst))

rango = list( range(10) )
print(rango)

# Calcular la hipotenusa de 100 triángulos rectángulos diferentes
# a = float(input('Ingrese cateto a:')
# b = float(input('Ingrese cateto b:')
# calculemos la hipotenusa de un triángulo rectángulo sabiendo la medida de ambos catetos 
# La hipotenusa de un triángulo rectángulo es igual a la raiz cuadrada de la suma del cuadrado de los catetos.
import math
for i in range(1,101):
  catetoA = i
  print("catetoA: %d" %catetoA)
  catetoB = i
  print("catetoB: %d" %catetoB)
  hipotenusa=math.sqrt((catetoA ** 2)+(catetoB ** 2))
  print("hipotenusa: %f" %hipotenusa)
print("i: %d" %i)

# -O-J-O- Revisar esto -O-J-O- 
# o bien se nos pide calcular la longitud de uno de los catetos conociendo la hipotenusa y el otro cateto.
# El cateto de un triángulo rectángulo es igual a la raiz cuadrada de la hipotenusa al cuadrado menos el otro cateto al cuadrado.
import math
for i in range(1, 101):
  catetoA = i
  print("catetoA: %d" %catetoA)
  hipotenusa = float(55)
  print("hipotenusa: %f" %hipotenusa)
  catetoB=math.sqrt((hipotenusa ** 2)-(catetoA ** 2))
  print("catetoB: %d" %catetoB)
print("i: %d" %i)

# Generar un número entre 5 y 10

rango = list(range(5,10))
print(rango) # -O-J-O- Ejecución: [5, 6, 7, 8, 9]

# Generar un rango de 10 a 0.

rango = list(range(10,0,-1))
print(rango) # -O-J-O- Ejecución: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]



