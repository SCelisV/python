# Lists are very similar to arrays. 
# They can contain any type of variable, and they can contain as many variables as you wish. 
# Lists can also be iterated over in a very simple manner. 
# Here is an example of how to build a list.

mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) #  -O-J-O- Ejecución 1
print(mylist[1]) #  -O-J-O- Ejecución 2
print(mylist[2]) #  -O-J-O- Ejecución 3

#  -O-J-O- Ejecución out 1,2,3
for x in mylist:
    print(x)

print("--------------------")
print("one list")
mylist = []
mylist.append("a")
mylist.append("b")
mylist.append("c")
print(mylist[0]) #  -O-J-O- Ejecución a
print(mylist[1]) #  -O-J-O- Ejecución b
print(mylist[2]) #  -O-J-O- Ejecución c
#  -O-J-O- Ejecución out a,b,c
x = 0
for x in mylist:
    print(x)

print("--------------------")
print("other list")
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) #  -O-J-O- Ejecución 1
print(mylist[1]) #  -O-J-O- Ejecución 2
print(mylist[2]) #  -O-J-O- Ejecución 3

#  -O-J-O- Ejecución out 1,2,3
for x in mylist:
    print("x: ", x)
    
print("--------------------")

# - O-J-O- Genera el siguiente error: - 
# 
# mylist = [1,2,3]
# print(mylist[10])

# Accessing an index which does not exist generates an exception (an error).

#     print(mylist[10])
# IndexError: list index out of range

# - O-J-O- Genera el siguiente error: - 

print("--------------------")
print ("second list")
numbers = [1, 2, 3, 4, 5]
strings = ["a", "b", "c", "d", "e"]
names = ["John", "Eric", "Jessica"]
second_name = names[1]

print(numbers)
print(strings)
print (names)
print("The second name on the names list is %s" % second_name)
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number),
    if (number % 2 == 0):
        print("es par")
    else:
        print("es impar")
print("Terminado")

#  -O-J-O- Ejecución out:
# [1, 2, 3, 4, 5]
# ['a', 'b', 'c', 'd', 'e']
# ['John', 'Eric', 'Jessica']
# The second name on the names list is Eric
# 1
# es impar
# 2
# es par
# 3
# es impar
# 4
# es par
# 5
# es impar
# Terminado

print("--------------------")
print ("three list")
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

#  -O-J-O- Ejecución out
# three list
# [1, 3, 5, 7, 2, 4, 6, 8]

print("--------------------")
print ("four list")
x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

#  -O-J-O- Ejecución out
# x_list contains 10 objects
# y_list contains 10 objects
# big_list contains 20 objects

# testing
print("testing some code: ")

if x_list.count(x) == 10 and y_list.count(y) == 10:
  print ("y..")
    
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")


###############
#  Excercise  #
###############

# In this exercise, you will need to add numbers and strings to the correct lists using the "append" list method. 
# You must add the numbers 1,2, and 3 to the "numbers" list, and the words 'hello' and 'world' to the strings variable.

# You will also have to fill in the variable second_name with the second name in the names list, using the brackets operator []. 

# Note that the index is zero-based, so if you want to access the second item in the list, its index will be 1.

numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
second_name = names[1]
numbers.append(1)
numbers.append(2)
numbers.append(3)
strings.append("hello")
strings.append("world")


# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

print("--------------------")

# listas creadas a partir de un rango: range.py => ver este fichero de ejemplos

# range (n...., n-1)
lista_00 = list(range (1,10))
print(f"este ćodigo: list(range (1,10)) crea una lista a partir usando la función range(rango): {lista_00}, comprobamos su tipo: {type(lista_00)}")

lista_00 = list(range (1,11))
print(f"este ćodigo: list(range (1,11)) crea una lista a partir usando la función range(rango): {lista_00}, comprobamos su tipo: {type(lista_00)}")

# métodos de una lista
# print(dir(lista_00))
# ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

print(f"con este código: len(lista_00), podemos saber cuantos elementos hay en el elemento lista_00: {len(lista_00)}")
print(f"con este código: len(lista_00), podemos saber cuantos elementos hay en el elemento lista_00: {len(lista_00)}")

print("--------------------")



# Ejemplos de listas.
numeros = [3,4,3,5,7,4,3,1,1]
ninjas = ['Naruto', 'Sakura', 'Sasuke', 'Hinata', 'Shikamaru']
mezcla = ['apple', 390, 876, 'orange', 'highway', 0.42, 87]

# Esto es una lista de listas que asignamos a la variable de nombre matriz
matriz = [[3,4,5], [1,2,3], [7,3,2]]

# Ejemplos de listas.
numeros = [3,4,3,5,7,4,3,1,1]
print("numeros: " + str(numeros))
# -O-J-O- Ejecución
# [3, 4, 3, 5, 7, 4, 3, 1, 1]

ninjas = ['Naruto', 'Sakura', 'Sasuke', 'Hinata', 'Shikamaru']
print("ninjas: " + str(ninjas))
# -O-J-O- Ejecución
# ['Naruto', 'Sakura', 'Sasuke', 'Hinata', 'Shikamaru']

mezcla = ['apple', 390, 876, 'orange', 'highway', 0.42, 87]
print("mezcla: " + str(mezcla))
# -O-J-O- Ejecución
# ['apple', 390, 876, 'orange', 'highway', 0.42, 87]

# Esto es una lista de listas que asignamos a la variable de nombre matriz
matriz = [[3,4,5], [1,2,3], [7,3,2]]
print("matriz: " + str(matriz))
print("\n")
# -O-J-O- Ejecución
# [[3, 4, 5], [1, 2, 3], [7, 3, 2]]

demo_list = [1, 'hello', 1.34, True, [1,2,3]]
colors = ['red', 'green', 'blue']

# - O-J-O- Genera el siguiente error: -

# numbers_list = list(1,2,3,4) => nos devuelve un error
# Traceback (most recent call last):
#   File "listas.py", line 34, in <module>
#     numbers_list = list(1,2,3,4)
# TypeError: list expected at most 1 arguments, got 4 # esperaba sólo un argumento, recibe 4

# para solucionarlo, lo que haremos es pasarle una tupla para agrupar los argumentos en 1 solo argumento
numbers_list = list((1,2,3,4))

print(f"demo_list: {str(demo_list)}; colors list: {colors}, and numbers_list: {numbers_list}, cuyo tipo es: {type(numbers_list)}" )

print(f"con este código: len(demo_list), podemos saber cuantos elementos hay en la list demo_list: {len(demo_list)}")

print(f"con este código: colors[1], podemos saber cual es el contenido de la posición 1 de la lista colors: {colors[1]}")

print(f"con este código: colors[-1], podemos saber cual es el contenido de la última posición(inverso) de la lista colors: {colors[-1]}")

print(f"con este código: 'green' in colors, podemos saber si un determinado elemento esta en la lista colors: {'green' in colors}" )

print(f"con este código: 'violet' in colors, podemos saber si un determinado elemento esta en la lista colors: {'violet' in colors}" )

print("con este código: colors[1]='violet', se cambia el valor a la posición 1 de la lista colors" )
colors[1] = "violet"

print(f"demo_list: {str(demo_list)}; colors list: {colors}, and numbers_list: {numbers_list}, cuyo tipo es: {type(numbers_list)}" )

# -O-J-O- Ejecución
# demo_list: [1, 'hello', 1.34, True, [1, 2, 3]]; colors list: ['red', 'green', 'blue'], and numbers_list: [1, 2, 3, 4], cuyo tipo es: <class 'list'>

# Para seleccionar un elemento por su índice
print(ninjas[0])
print(ninjas[-1])
print(matriz[0])
# -O-J-O- Ejecución
# Naruto
# Shikamaru
# [3, 4, 5]

# Para seleccionar un elemento por su índice
print("ninjas[0]: " + str(ninjas[0]))
print("ninjas[-1]: " + str(ninjas[-1]))
print("matriz[0]: " + str(matriz[0]))

# -O-J-O- Ejecución
# ninjas[0]: Naruto
# ninjas[-1]: Shikamaru
# matriz[0]: [3, 4, 5]

# lista[start: stop: step]
print(ninjas[::2])
print(ninjas[1: 4])
print(ninjas[::-1])
# -O-J-O- Ejecución
# ['Naruto', 'Sasuke', 'Shikamaru']
# ['Sakura', 'Sasuke', 'Hinata']
# ['Shikamaru', 'Hinata', 'Sasuke', 'Sakura', 'Naruto']

# lista[start: stop: step]
print("step: -> ninjas[::2]: " + str(ninjas[::2]))
# -O-J-O- Ejecución
# step: -> ninjas[::2]: ['Naruto', 'Sasuke', 'Shikamaru']
print("\n")

print("start: stop -> ninjas[1: 4]: " + str(ninjas[1: 4]))
# -O-J-O- Ejecución
# start: stop -> ninjas[1: 4]: ['Sakura', 'Sasuke', 'Hinata']
print("\n")
print("start: -> ninjas[::-1]: " + str(ninjas[::-1]))
# -O-J-O- Ejecución
# start: -> ninjas[::-1]: ['Shikamaru', 'Hinata', 'Sasuke', 'Sakura', 'Naruto']
print("\n")
print("start: -> matriz[1:2:3]: " + str(matriz[1:2:3]))
# -O-J-O- Ejecución
# start: -> matriz[1:2:3]: [[1, 2, 3]]
print("\n")


# añadir un elemento nuevo al final de un lista
print(ninjas)
ninjas.append('Kakashi')
print(ninjas)
# -O-J-O- Ejecución
# ['Naruto', 'Sakura', 'Sasuke', 'Hinata', 'Shikamaru']['Naruto', 'Sakura', 'Sasuke', 'Hinata', 'Shikamaru', 'Kakashi']

print("\n")
print("add un elemento a la lista ninjas: ninjas.append('Kakashi'): \n" + str(ninjas))
# -O-J-O- Ejecución
# add un elemento a la lista ninjas: ninjas.append('Kakashi'):
# ['Naruto', 'Sakura', 'Sasuke', 'Hinata', 'Shikamaru', 'Kakashi']


# sumar listas
estudiantes = ['Harry', 'Hermione', 'Ron']
profesores = ['Dumbledore', 'Severus', 'Hagrid']
print(estudiantes)
print(profesores)
hogwards = estudiantes + profesores
print(hogwards)
# -O-J-O- Ejecución
# ['Harry', 'Hermione', 'Ron']
# ['Dumbledore', 'Severus', 'Hagrid']
# ['Harry', 'Hermione', 'Ron', 'Dumbledore', 'Severus', 'Hagrid']


# sumar listas
estudiantes = ['Harry', 'Hermione', 'Ron']
print("estudiantes: \n" + str(estudiantes))
profesores = ['Dumbledore', 'Severus', 'Hagrid']
print("profesores: \n" + str(profesores))
hogwards = estudiantes + profesores
print("hogwards = estudiantes + profesores: \n" + str(hogwards))
# -O-J-O- Ejecución
# estudiantes:
# ['Harry', 'Hermione', 'Ron']
# profesores:
# ['Dumbledore', 'Severus', 'Hagrid']
# hogwards = estudiantes + profesores:
# ['Harry', 'Hermione', 'Ron', 'Dumbledore', 'Severus', 'Hagrid']


# media de un conjunto de números
numeros = [34, 12, 93, 783, 330, 896, 1, 55]
suma = sum(numeros)
longitud = len(numeros)
media = suma / longitud
print(media)
# -O-J-O- Ejecución
# 275

# media de un conjunto de numeros
numeros = [34, 12, 93, 783, 330, 896, 1, 55]
print("numeros: \n" + str(numeros))
suma = sum(numeros)
print("sum(numeros): \n" + str(suma))
longitud = len(numeros)
print("len(numeros): \n" + str(longitud))
media = suma / longitud
print ("sum / len: \n %f" %(media) )
# -O-J-O- Ejecución
# numeros:
# [34, 12, 93, 783, 330, 896, 1, 55]
# sum(numeros):
# 2204
# len(numeros):
# 8
# sum / len:
# 275.000000


# mínimo y máximo
minimo = min(numeros)
maximo = max(numeros)
print(minimo)
print(maximo)
# -O-J-O- Ejecución
# 1
# 896

# minimo y maximo
numeros = [34, 12, 93, 783, 330, 896, 1, 55]
# print("numeros: \n" + str(numeros))
minimo = min(numeros)
print ("min(numeros): \n %d" %(minimo) )
maximo = max(numeros)
print("max(numeros): \n %d" %(maximo) )
# -O-J-O- Ejecución
# min(numeros):
#  1
# max(numeros):
#  896


# Ordenación
numeros_ordenados = sorted(numeros)
print(numeros_ordenados)
# -O-J-O- Ejecución
# [1, 12, 34, 55, 93, 330, 783, 896]


# Ordenacion
numeros = [34, 12, 93, 783, 330, 896, 1, 55]
# print("numeros: \n" + str(numeros))
numeros_ordenados = sorted(numeros)
print("sorted(numeros):\n " + str(numeros_ordenados))
# -O-J-O- Ejecución
# sorted(numeros):
#  [1, 12, 34, 55, 93, 330, 783, 896]


# métodos de las lista
# print(dir(colors))
# ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__',
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

print("--------------------")

print(colors)
print("insertar un elemento nuevo en la lista: colors.append('yellow') -> ")
colors.append("yellow")
print(colors)

# -O-J-O- Ejecución
# ['red', 'violet', 'blue']
# insertar un elemento nuevo en la lista: colors.append('yellow') ->
# ['red', 'violet', 'blue', 'yellow']

print("--------------------")

print(colors)
print("insertar más de un elemento nuevo en la lista usando una Tupla: colors.append(('yellow', 'black')) -> ")
colors.append(('yellow', 'black'))
print(colors)
print("insertar más de un elemento nuevo en la lista usando una Lista: colors.append(['yellow', 'black']) -> ")
colors.append(['yellow', 'black'])
print(colors)
print("insertar más de un elemento nuevo en la lista usando extend: colors.extend(('white', 'black', 'yellow')) -> ")
colors.extend(('white', 'black', 'yellow'))
print(colors)

# -O-J-O- Ejecución

# ['red', 'violet', 'blue', 'yellow']
# insertar más de un elemento nuevo en la lista usando una Tupla: colors.append(('yellow', 'black')) ->
# ['red', 'violet', 'blue', 'yellow', ('yellow', 'black')]
# insertar más de un elemento nuevo en la lista usando una Lista: colors.append(['yellow', 'black']) ->
# ['red', 'violet', 'blue', 'yellow', ('yellow', 'black'), ['yellow', 'black']]
# insertar más de un elemento nuevo en la lista usando extend: colors.extend(('white', 'black', 'yellow')) ->
# ['red', 'violet', 'blue', 'yellow', ('yellow', 'black'), ['yellow', 'black'], 'white', 'black', 'yellow']

# - O-J-O- Genera el siguiente error: -

# colors.extend('white', 'black', 'yellow')

#     colors.extend('white', 'black', 'yellow')
# TypeError: extend() takes exactly one argument (3 given)

# - O-J-O- Genera el siguiente error: -

# colors.append('yellow', 'black')

#     colors.append('yellow', 'black')
# TypeError: append() takes exactly one argument (2 given)

# - O-J-O- Genera el siguiente error: -

print("--------------------")

print(colors)
print("insertar un elemento a partir de una posición específica dentro de la lista ->  colors.insert(2, 'green') -> ")
colors.insert(2, 'green')
print(colors)
print("insertar un elemento a partir de una posición (inversa) específica dentro de la lista ->  colors.insert(-2, 'gray') -> ")
colors.insert(-2, 'gray')
print(colors)
print("insertar un elemento en la última posición dentro de la lista ->  colors.insert(len(colors), 'orange') -> ")
colors.insert(len(colors), 'orange')
print(colors)


# -O-J-O- Ejecución

# ['red', 'violet', 'blue', 'yellow', ('yellow', 'black'), ['yellow', 'black'], 'white', 'black', 'yellow']
# insertar un elemento a partir de una posición específica dentro de la lista ->  colors.insert(2, 'green') ->
# ['red', 'violet', 'green', 'blue', 'yellow', ('yellow', 'black'), ['yellow', 'black'], 'white', 'black', 'yellow']
# insertar un elemento a partir de una posición (inversa) específica dentro de la lista ->  colors.insert(2, 'green') ->
# ['red', 'violet', 'green', 'blue', 'yellow', ('yellow', 'black'), ['yellow', 'black'], 'white', 'gray', 'black', 'yellow']
# insertar un elemento en la última posición dentro de la lista ->  colors.insert(len(colors), 'orange') ->
# ['red', 'violet', 'green', 'blue', 'yellow', ('yellow', 'black'), ['yellow', 'black'], 'white', 'gray', 'black', 'yellow', 'orange']

print("--------------------")

print("remover el último elemento de una lista ->  colors.pop() -> ")
print(colors)
colors.pop()
print(colors)
print("remover un elemento especifico de una lista por el valor ->  colors.remove(('yellow', 'black')) -> ")
colors.remove(('yellow', 'black'))
print(colors)
print("remover un elemento especifico de una lista por el valor ->  colors.remove(['yellow', 'black']) -> ")
colors.remove(['yellow', 'black'])
print(colors)
print("remover un elemento especifico de una lista por el valor ->  colors.remove('yellow') -> ")
colors.remove('yellow')
print(colors)
print("remover un elemento especifico de una lista por la posición ->  colors.pop(1) -> ")
colors.pop(1)
print(colors)
print("remover a partir de una posición ->  colors.pop(3, ) -> ")
colors.pop(3, )
print(colors)
print("remover ToDos los elementos de la lista ->  colors.clear() -> ")
# colors.clear()
print(colors)


# -O-J-O- Ejecución
# remover el último elemento de una lista ->  colors.pop() ->
# ['red', 'violet', 'green', 'blue', 'yellow', ('yellow', 'black'), ['yellow', 'black'], 'white', 'gray', 'black', 'yellow', 'orange']
# ['red', 'violet', 'green', 'blue', 'yellow', ('yellow', 'black'), ['yellow', 'black'], 'white', 'gray', 'black', 'yellow']
# remover un elemento especifico de una lista por el valor ->  colors.remove(('yellow', 'black')) ->
# ['red', 'violet', 'green', 'blue', 'yellow', ['yellow', 'black'], 'white', 'gray', 'black', 'yellow']
# remover un elemento especifico de una lista por el valor ->  colors.remove(['yellow', 'black']) ->
# ['red', 'violet', 'green', 'blue', 'yellow', 'white', 'gray', 'black', 'yellow']
# remover un elemento especifico de una lista por el valor ->  colors.remove('yellow') ->
# ['red', 'violet', 'green', 'blue', 'white', 'gray', 'black', 'yellow']
# remover un elemento especifico de una lista por la posición ->  colors.pop(1) ->
# ['red', 'green', 'blue', 'white', 'gray', 'black', 'yellow']
# remover a partir de una posición ->  colors.pop(3, ) ->
# ['red', 'green', 'blue', 'gray', 'black', 'yellow']
# remover ToDos los elementos de la lista ->  colors.clear() ->
# []


# - O-J-O- Genera el siguiente error: -

# colors.remove('black', 'yellow')

#     colors.remove('black', 'yellow')
# TypeError: remove() takes exactly one argument (2 given)

print("--------------------")

print("Ordenar la lista ->  colors.sort() -> ")
print(colors)
colors.sort()
print(colors)
print("Ordenar la lista descendente ->  colors.sort(reverse=True) -> ")
colors.sort(reverse=True)
print(colors)
print("Obtener el indice de un elemento de la lista ->  (colors.index('gray') -> ")
print(colors.index('gray'))
print("Contar los elementos de la lista ->  colors.count('blue') -> ")
print(colors.count('blue'))



# -O-J-O- Ejecución

# Ordenar la lista ->  colors.sort() ->
# ['red', 'green', 'blue', 'gray', 'black', 'yellow']
# ['black', 'blue', 'gray', 'green', 'red', 'yellow']
# Ordenar la lista descendente ->  colors.sort(reverse=True) ->
# ['yellow', 'red', 'green', 'gray', 'blue', 'black']
# Obtener el indice de un elemento de la lista ->  colors.index('gray') ->
# 3
# Contar los elementos de la lista ->  colors.count('blue') ->
# 1


print("--------------------")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IN-WORK-OUT
Created on Thu Sep 10 18:28:17 2020

@author: scelis - ¯\_(ツ)_/¯

List are an ordered sequence - MUTABLE, as comma-separated within parentheses []

integers, strings, float and other lists pueden ser contenidos en una list
list.py
"""

# The address of each element within a list is called an index
# Indexing
# the list within square brackets [ ], with your content inside the parenthesis and separated by commas
# We can use negative and regular indexing
L=["Michael Jackson", 10.1, 1982]
# 'Michael Jackson'
L[0]
L[-3]

# 10.1
L[1]
L[-2]

# 1982
L[2]
L[-1]

# We can nest other lists - listas anidadas
L=["Michael Jackson", 10.1, 1982, [1,2],('A',1)]
# 'Michael Jackson'
L[0]
# 10.1
L[1]
# 1982
L[2]
# [1, 2]
L[3]
# 1
L[3][0]
# 2
L[3][1]

# ('A', 1)
L[4]
# 'A'
L[4][0]
# 1
L[4][1]

# Slicing -  the last two elements
L[3:5] # [[1, 2], ('A', 1)]

# Concatenar una lista con (+)
L1=L+["pop", 10] # ['Michael Jackson', 10.1, 1982, [1, 2], ('A', 1), 'pop', 10]

A1 = [1, 'a']
B1= [2, 1, 'd']
A1 = A1+B1
A1 # [1, 'a', 2, 1, 'd']

# extend lo que hace es add dos elementos a la lista existente
# add new elements to the list
L.extend(["rock",20]) # ['Michael Jackson', 10.1, 1982, [1, 2], ('A', 1), 'rock', 20]

# Use extend to add elements to list - we apply extend we add two new elements to the list
L2 = [ "Michael Jackson", 10.2]
L2.extend(['pop', 10])
L2 # ['Michael Jackson', 10.2, 'pop', 10]

A2 = [1, 'a']
B2 = [2, 1, 'd']
A2.extend(B2)
A2 # [1, 'a', 2, 1, 'd']

# we apply append add one element to the list - have one new element
L.append(["rock",20]) # ['Michael Jackson', 10.1, 1982, [1, 2], ('A', 1), 'rock', 20, ['rock', 20]]

L.append(["pop",10])
# ['Michael Jackson',
#  10.1,
#  1982,
#  [1, 2],
#  ('A', 1),
#  'rock',
#  20,
#  ['rock', 20],
#  ['pop', 10]]

# we have one new element
L3 = [ "Michael Jackson", 10.2]
L3.append(['a','b'])
L3 # ['Michael Jackson', 10.2, ['a', 'b']]
len(L3)
type(L3)
# Change the element based on the index
A = ["disco", 10, 1.2]
print('Antes cambio:', A) # Antes cambio: ['disco', 10, 1.2]
A[0] = 'hard rock'
print('Después cambio:', A) # Después cambio: ['hard rock', 10, 1.2]

# elimina, borra un elemento de la lista
print('Antes cambio:', A) # Antes cambio: ['hard rock', 10, 1.2]
del(A[1])
print('Después cambio:', A) # Después cambio: ['hard rock', 1.2]


# split - Convert String to list, # Split the string, default is by space ""
"Michael Jackson".split() # ['Michael', 'Jackson']

# Split the string by comma
"A,B,C,D".split(",") # ['A', 'B', 'C', 'D']

# When we set one variable B equal to A; both A and B are referencing the same list in memory:
# Alias, are reference at the same list

A=["hard rock", 10,1.2]
B=A
print('A:', A) # A: ['hard rock', 10, 1.2]
print('B:', B) # B: ['hard rock', 10, 1.2]

A[0] # 'hard rock'
# ['hard rock', 10, 1.2]
B[0] # 'hard rock'

# Examine the copy by reference
print('B[0]:', B[0]) # B[0]: hard rock
A[0] = "banana"
print('B[0]:', B[0]) # B[0]: banana


# Clone, crea una new list, reference a diferentes list
# Clone (clone by value) the list A then Variable B references a new copy or clone of the original lis
A=["hard rock", 10,1.2]
print('A:', A) # A: ['hard rock', 10, 1.2]
B=A[:]
print('B:', B) # B: ['hard rock', 10, 1.2]

print('A:', A) # A: ['hard rock', 10, 1.2]
print('A[0]:', A[0]) # A[0]: banana
print('B[0]:', B[0]) # B[0]: hard rock

# Change the first element of the list to an uppercase
B[0].upper() # 'HARD ROCK'

# Help on class list in module builtins:
help(A)
# or
help(list)
# because
type(A) # list


print("--------------------")
