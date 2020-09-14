"""
@author: scelis - ¯\_(ツ)_/¯
"""
##########################################
# Primer ejemplo: range                  #
# numero empieza 0 < 10 e incremento en 1#
##########################################
print(range(3)) # range(0, 3)

for numero in range(10):
	print(numero)

for i in range(0,5):
    print("i: ", [i])

# O-J-O Ejecucion 
# i:  [0]
# i:  [1]
# i:  [2]
# i:  [3]
# i:  [4]
    
# Primer ejemplo: range
# numero empieza 0 < 10 e incremento en 1
for numero in range(10):
  print("numero: " + str(numero) + " ")

# O-J-O Ejecucion 
# numero: 0
# numero: 1
# numero: 2
# numero: 3
# numero: 4
# numero: 5
# numero: 6
# numero: 7
# numero: 8
# numero: 9

############################################
# Segundo ejemplo: range(start: stop: step)#
# numero empieza 5 < 15 e incrementa en 2  #
############################################

for numero in range(5, 15, 2):
	print(numero)
  
# O-J-O Ejecucion 
# 5
# 7
# 9
# 11
# 13

# Segundo ejemplo: range(start: stop: step)
# numero empieza 5 < 15 e incrementa en 2
for numero in range(5, 15, 2):
	print("numero: " + str(numero))

# O-J-O Ejecucion 
# numero: 5
# numero: 7
# numero: 9
# numero: 11
# numero: 13

#####################################
# Tercer ejemplo                    #
# Recorre la lista                  #
#####################################

ninjas = ['Naruto', 'Sakura', 'Sasuke', 'Hinata', 'Shikamaru']
for ninja in ninjas: 
	print(ninja)

#OJO - Ejecucion
# Naruto
# Sakura
# Sasuke
# Hinata
# Shikamaru

ninjas = ['Naruto', 'Sakura', 'Sasuke', 'Hinata', 'Shikamaru']
print("ninjas: \n" + str(ninjas))

for ninja in ninjas: 
	print("ninja: " + str(ninja))

# O-J-O Ejecucion 
# ninjas:
# ['Naruto', 'Sakura', 'Sasuke', 'Hinata', 'Shikamaru']
# ninja: Naruto
# ninja: Sakura
# ninja: Sasuke
# ninja: Hinata
# ninja: Shikamaru

#######################################
# Cuarto ejemplo                      #
# Recorre un diccionario {clave:valor}#
#######################################

valoraciones = {'Alien':9.5, 'Terminator 2':8.9, 'Arma Letal':7.3}
print("diccionario valoraciones: \n" + str(valoraciones))
print("metodo para extraer las keys en el diccionario: \nvaloraciones.keys():  \n")

# Imprime los nombres de las pelis - keys del diccionario
for peli in valoraciones.keys(): 
	print("pelicula: " + peli)

# Imprime los valores de las pelis - values del diccionario
print("\nmetodo para extraer los values en el diccionario: \nvaloraciones.values(): \n")
for valoracion in valoraciones.values(): 
	print("valoracion: " + str(valoracion))

# Imprime el diccionario valoraciones - keys, values
print("\nmetodo para ver los items del diccionario: \nvaloraciones.items(): \n")
for peli, puntuacion in valoraciones.items(): 
	print(peli, "tiene una puntuacion de: ", puntuacion)


# O-J-O Ejecucion 
# diccionario valoraciones:
# {'Alien': 9.5, 'Terminator 2': 8.9, 'Arma Letal': 7.3}
# metodo para extraer las keys en el diccionario:
# valoraciones.keys():
#
# pelicula: Alien
# pelicula: Terminator 2
# pelicula: Arma Letal

# metodo para extraer los values en el diccionario:
# valoraciones.values():

# valoracion: 9.5
# valoracion: 8.9
# valoracion: 7.3

# metodo para ver los items del diccionario:
# valoraciones.items():

# ('Alien', 'tiene una puntuacion de: ', 9.5)
# ('Terminator 2', 'tiene una puntuacion de: ', 8.9)
# ('Arma Letal', 'tiene una puntuacion de: ', 7.3)

######################################
# Quinto ejemplo: calculo de la suma #
# de una lista de numeros            #
######################################

numeros = [34, 12, 93, 783, 330, 896, 1, 55]
total = 0
for numero in numeros: 
	total += numero
print(total)

# O-J-O Ejecucion 
# 2204

# Quinto ejemplo: calculo de la suma
numeros = [34, 12, 93, 783, 330, 896, 1, 55]
print("numeros: \n" + str(numeros) + "\n")
total = 0
# Recorre la lista numeros y calcula su suma
for numero in numeros: 
	total += numero
print("total: " + str(total))

# O-J-O Ejecucion 
# numeros:
# [34, 12, 93, 783, 330, 896, 1, 55]

# total: 2204

# Sexto ejemplo:
# range(start: stop: step) 
lista = []
print("lista: " + str(lista))
# x start:2 stop: 6
for x in range(2, 6): 
  numero = x**2
  print("numero: " + str (numero) + " es el cuadrado (x**2) de x: " + str(x))
  lista.append(numero)
  print("adiciona el numero a la lista: lista.append(numero): ")
  print("lista: " + str(lista) + "\n")


# O-J-O Ejecucion 
# lista: []
# numero: 4 es el cuadrado (x**2) de x: 2
# adiciona el numero a la lista: lista.append(numero):
# lista: [4]

# numero: 9 es el cuadrado (x**2) de x: 3
# adiciona el numero a la lista: lista.append(numero):
# lista: [4, 9]

# numero: 16 es el cuadrado (x**2) de x: 4
# adiciona el numero a la lista: lista.append(numero):
# lista: [4, 9, 16]

# numero: 25 es el cuadrado (x**2) de x: 5
# adiciona el numero a la lista: lista.append(numero):
# lista: [4, 9, 16, 25]

######################################
# Séptimo ejemplo: Bucle doble
######################################
valoraciones = {'Alien':9.5, 'Terminator 2':8.9, 'Arma Letal':7.3}
estudiantes = ['Harry', 'Hermione', 'Ron']
for estudiante in estudiantes: 
	for peli, valoracion in valoraciones.items(): 
		print(estudiante, "vio", peli, "y le puso una nota de", valoracion)

# O-J-O Ejecucion 
# ('Harry', 'vio', 'Alien', 'y le puso una nota de', 9.5)
# ('Harry', 'vio', 'Terminator 2', 'y le puso una nota de', 8.9)
# ('Harry', 'vio', 'Arma Letal', 'y le puso una nota de', 7.3)
# ('Hermione', 'vio', 'Alien', 'y le puso una nota de', 9.5)
# ('Hermione', 'vio', 'Terminator 2', 'y le puso una nota de', 8.9)
# ('Hermione', 'vio', 'Arma Letal', 'y le puso una nota de', 7.3)
# ('Ron', 'vio', 'Alien', 'y le puso una nota de', 9.5)
# ('Ron', 'vio', 'Terminator 2', 'y le puso una nota de', 8.9)
# ('Ron', 'vio', 'Arma Letal', 'y le puso una nota de', 7.3)


for i in range(5):
  print ('A number:', i)

# -O-J-O- Ejecución 
#A number: 0
#A number: 1
#A number: 2
#A number: 3
#A number: 4



print("--------------------")
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)

# -O-J-O- Ejecución 
# 2
# 3
# 5
# 7


print("--------------------")
count = 0
a = [2, 2, 2, 1, 6, 8, 2, 4]
for i in a:
    if i == 2:
        count = count + 1
print("La cuenta total es %d: " %count) # -O-J-O- Ejecución La cuenta total es 4:

print("--------------------")


for e in range(len(a)):
    print(e,a[e])
    # -O-J-O- Ejecución 
    # 0 2
    # 1 2
    # 2 2
    # 3 1
    # 4 6
    # 5 8
    # 6 2
    # 7 4   
    if e == 2:
        count = count + 1
print("La cuenta total es: " + str(count)) # -O-J-O- Ejecución La cuenta total es: 5

print("--------------------")
for x in range(5):
    print(x)
    # -O-J-O- Ejecución 
    # 0
    # 1
    # 2
    # 3
    # 4

print("--------------------")

for x in range(3, 6):
    print(x)
    # -O-J-O- Ejecución 
    # 3
    # 4
    # 5


print("--------------------")
for x in range(3, 8, 2):
    print(x)
    # -O-J-O- Ejecución 
    # 3
    # 5
    # 7

######################################
# Bucle de listas anidadas           # 
######################################

print("--------------------")
#suma cada componente de la lst1 con cada componente de lst2 
lst1=[i for i in range(1, 11)]
lst2=[j for j in range(1, 11)]
lst3=[]
total = 0
print ("lst1: " + str(lst1)) # -O-J-O- Ejecución lst1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print ("lst2: " + str(lst2)) # -O-J-O- Ejecución lst2: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in lst1:
  for y in lst2:
    z = (x + y)
    lst3.append(z)
    total += z
print (lst3) # -O-J-O- Ejecución [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print ("total: " + str(total)) # -O-J-O- Ejecución total: 1100


# Python code to demonstrate range() vs xrange() - no funciona en Python 3.7.4
# on  basis of return type 
  
# initializing a with range() 
a = range(1,10000) 
  
# initializing a with range() 
x = range(1,10000) 

# # initializing a with xrange() 
# x = xrange(1,10000) 

# testing the type of a 
print ("The return type of range() is : ") 
print (type(a)) 
  
# testing the type of x 
print ("The return type of xrange() is : ") 
print (type(x)) 

# O-J-O- Ejecucion
# The return type of range() is :
# <type 'list'>
# The return type of xrange() is :
# <type 'xrange'>

# "while" loops
# While loops repeat as long as a certain boolean condition is met.

count = 0
while count < 5:
    print(count)
    count += 1  # This is the same as count = count + 1

# O-J-O- Ejecucion

# 0
# 1
# 2
# 3
# 4

# "break" and "continue" statements
# break is used to exit a for loop or a while loop, whereas continue is used to skip the current block, and return to the "for" or "while" statement. 

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break


# O-J-O- Ejecucion
# 0
# 1
# 2
# 3
# 4

for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)
	
# O-J-O- Ejecucion: Only odd (IMPAR)
# 1
# 3
# 5
# 7
# 9

# can we use "else" clause for loops?
# unlike languages like C,CPP.. we can use else for loops. 
# When the loop condition of "for" or "while" statement fails then code part in "else" is executed. 
# If break statement is executed inside for loop then the "else" part is skipped. 
# Note that "else" part is executed even if there is a continue statement

# O-J-O- Ejecucion
# Prints out 0,1,2,3,4 and then it prints "count value reached 5"

count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))


for i in range(1, 10):
    a=i%5
    print("i: %d - a: %f " % (i, a)) 
    if(i%5==0):
      print("break: ")
      break
else:
    print("this is not printed because for loop is terminated because of break but NOT FOR A WRONG condition")

# O-J-O- Ejecucion
# i: 1 - a: 1.000000
# i: 2 - a: 2.000000
# i: 3 - a: 3.000000
# i: 4 - a: 4.000000
# i: 5 - a: 0.000000
# break:

# Let’s say we would like to iterate through list dates and stop at the year 1973, then print out the number of iterations. This can be done with the following block of code:

# While Loop Example
dates = [1982, 1980, 1973, 2000]

i = 0
year = 0

while(year != 1973):
    year = dates[i]
    i = i + 1
    print(year)

print("It took ", i ,"repetitions to get out of loop.")    

# 1982
# 1980
# 1973
# It took  3 repetitions to get out of loop.

# Imprime los valores de una lista con while loop
# display the values of the Rating of an album playlist stored in the list PlayListRatings
PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
score = PlayListRatings[0]
i = 0
while(score >= 6):
    print ("i:", i, "score:",PlayListRatings[i]) 
    i+=1
    score = PlayListRatings[i]
print("este es el primer menor que 6", "i:", i, "score:",PlayListRatings[i])

# i: 0 score: 10
# i: 1 score: 9.5
# i: 2 score: 10
# i: 3 score: 8
# i: 4 score: 7.5
# este es el primer menor que 6 i: 5 score: 5

squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0
while(squares[i] == 'orange'):
    new_squares.append(squares[i])
    i = i + 1
print (new_squares)
# ['orange', 'orange']

squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
len(squares)
type(squares)
new_squares = []
i=0
color = squares[i]
print(color, type(color))
while(color == 'orange'):
    print(color)
    i += 1
    new_squares.append(color)
    color = squares[i]
print("new_squares", new_squares)
# new_squares ['orange', 'orange']

###############
#  Excercise  #
###############

# Loop through and print out all even numbers from the numbers list in the same order they are received. 
# Don't print any numbers that come after 237 in the sequence.

numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]
for i in numbers:
    if (i == 237):
      break
    # Check if i is even
    if (i % 2 == 0):
        print("i: %d" % i)
    else:
      continue

# -O-J-O- Ejecución
# i: 402	     
# i: 984	     
# i: 360	     
# i: 408	     
# i: 980	     
# i: 544	     
# i: 390	     
# i: 984	     
# i: 592	     
# i: 236	     
# i: 942	     
# i: 386	     
# i: 462	     
# i: 418	     
# i: 344	     
# i: 236	     
# i: 566	     
# i: 978	     
# i: 328	     
# i: 162	     
# i: 758	     
# i: 918	     


# Otra forma:
for number in numbers:
    if number == 237:
        break

    if number % 2 == 1:
        continue

    print(number)

# -O-J-O- Ejecución
# 402
# 984
# 360
# 408
# 980
# 544
# 390
# 984
# 592
# 236
# 942
# 386
# 462
# 418
# 344
# 236
# 566
# 978
# 328
# 162
# 758
# 918

print("--------------------")

foods = ['apples', 'bread', 'cheese', 'milk', 'bananas', 'graves']

for food in foods:
    if food == 'cheese':
        print(f"you have to buy this product: {food}")
    print(food)

# -O-J-O- Ejecución

# apples
# bread
# you have to buy this product: cheese
# cheese
# milk
# bananas
# graves

print("--------------------")

# For loop example

dates = [1982,1980,1973]
N = len(dates)

for i in range(N):
    print(dates[i])   

# -O-J-O- Ejecución
# 1982
# 1980
# 1973

# Use for loop to change the elements in list
squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i in range(0, 5):
    print("Antes square ", i, 'is',  squares[i])
    squares[i] = 'weight'
    print("Despues square ", i, 'is',  squares[i])
    
# access the index and the elements of a list 
# Loop through the list and iterate on both index and element value
squares=['red', 'yellow', 'green', 'purple', 'blue']

# i is the index 
# square is the element in the list
# imprime el indice y el elemento de la lista a la vez
for i, square in enumerate(squares):
    print(i, square)    
    
# 0 red
# 1 yellow
# 2 green
# 3 purple
# 4 blue    

# the elements
Genres = ['rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for i in Genres:
    print(i)


#the elements and index
Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for i, j in enumerate(Genres):
    print(i, j)


# all the element between -5 and 5 
for i in range(-5,6):
    print(i)