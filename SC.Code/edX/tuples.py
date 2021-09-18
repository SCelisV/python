#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IN-WORK-OUT
Created on Thu Sep 10 16:44:35 2020

@author: scelis - ¯\_(ツ)_/¯

Tuples are an ordered sequence - IMMUTABLE, as comma-separated within parentheses ()

string, integer and float pueden ser contenidos en una tupla

tuples.py

"""
# This is a tuple
Ratings=(10,9,6,5,10,8,9,6,2)
# tuple
type(Ratings)

tuple1=("disk",10,1.2)
# tuple
type(tuple1)

# Each element of a tuple can be accessed via an index.
tuple1[0] # 'disk'
print(type(tuple1[0])) # <class 'str'>

tuple1[1] # 10

tuple1[2] # 1.2

# We can also use negative indexing
# We can obtain the last element 
tuple1[-1] # 1.2

tuple1[-2] # 10

tuple1[-3] # 'disk'

# Concatenate Tuples + ('disk', 10, 1.2, 'hard rock', 10)
tuple2 = tuple1 + ("hard rock", 10)

# Slicing - We can slice tuples obtaining multiple values
tuple2[0:3] # from index 0 to index 2 ('disk', 10, 1.2)
tuple2[3:5] # from index 3 to index 4 ('hard rock', 10)

# Get the length - longitud of tuple
len(tuple2) # 5

# No se crea una nueva tupla, se hace una referencia a la existente
Ratings1 = Ratings
# 6
Ratings[2]
# (2, 10, 1)
Ratings=(2,10,1)
# Sort - Ordenar the tuple - [1, 2, 10]
RatingsSorted=sorted(Ratings)

# Nesting - anidadas . an Tuple can contain another tuple as well as other more complex data types
NestedT=(1,2,("pop","rock"),(3,4),("disk",(1,2)))


len(NestedT) # longitud de la tupla


print("Element 0 of Tuple: ", NestedT[0]) # Element 0 of Tuple:  1


NestedT[1] # 2

# Each element in the tuple including other tuples can be obtained via an index 
print("Element 2 of Tuple: ", NestedT[2]) # Element 2 of Tuple:  ('pop', 'rock')

NestedT[2][0] # 'pop'

NestedT[2][1] # 'rock'
# Print the first element in the second nested tuples
NestedT[2][1][0] # 'r'
NestedT[3] # (3, 4)

NestedT[3][0] # 3

print("Element 3, 1 of Tuple: ",   NestedT[3][1]) # Element 3, 1 of Tuple:  4

NestedT[4] # ('disk', (1, 2))   

NestedT[4][0] # 'disk'

NestedT[4][1] # (1, 2)
# Print the first element in the second nested tuples
NestedT[4][1][0] # 1
# Print the second element in the second nested tuples
NestedT[4][1][1] # 2

genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock", \
                "R&B", "progressive rock", "disco") 


# Find the length of the tuple
len(genres_tuple) # 8

# last element of the tuple
genres_tuple[-1] # 'disco'
genres_tuple[7] # 'disco'

# Access the element, with respect to index 3: 
genres_tuple[3]   

# Use slicing to obtain indexes 3, 4 and 5:
genres_tuple[3:6]      

# Find the first two elements of the tuple:
genres_tuple[:2]    

# Find the first index of "disco":
genres_tuple.index("disco")

C_tuple=(-5, 1, -3)
C_tupleSorted=sorted(C_tuple)
print(C_tupleSorted) # [-5, -3, 1]

# tuplas.py => inmutables

print("definir una tupla: -> x = (1, 2, 3)")
x = (1, 2, 3)
print(f"esto es una tupla: {x}, el tipo de este objeto es: {type(x)}")
print("definir una tupla: -> y = tuple((1,2,3,4))")
y = tuple((1,2,3,4))
print(f"esto es una tupla: {y}, el tipo de este objeto es: {type(y)}")
print("definir una tupla de un sólo elemento: -> z = (1,)")
z = (1,)
print(f"{z} es una tupla de un solo elemento, el tipo de este objeto es: {type(z)}")
print(f"x[0] => para acceder a el contenido de una posición de la tupla: {x[0]} ")
print(f"x[02] => para acceder a el contenido de una posición de la tupla: {x[2]} ")
print(f"para eliminar una tupla => del(x)")
del(x)

# Caso de uso de como se define una tupla, longitud y latitud de ciudades dentro de un dictionary
locations = {
    (35.1213, 39.000): "Tokio",
    (35.1213, 39.000): "NY"
}
print(f"Caso de uso: Definir un dictionary location con tuplas que contengan la longitud y la latitud de una ciudad, por ejemplo..: is {type(locations)}")


# - O-J-O- Genera el siguiente error: -

# x[2] = 3

#     x[2] = 3
# TypeError: 'tuple' object does not support item assignment

# print(dir(y)) - metodos
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
# 'count', 'index']

# -O-J-O- Ejecución

# definir una tupla: -> x = (1, 2, 3)
# esto es una tupla: (1, 2, 3), el tipo de este objeto es: <class 'tuple'>
# definir una tupla: -> y = tuple((1,2,3,4))
# esto es una tupla: (1, 2, 3, 4), el tipo de este objeto es: <class 'tuple'>
# definir una tupla de un sólo elemento: -> z = (1,)
# (1,) es una tupla de un solo elemento, el tipo de este objeto es: <class 'tuple'>
# x[0] => para acceder a el contenido de una posición de la tupla: 1
# x[02] => para acceder a el contenido de una posición de la tupla: 3
# para eliminar una tupla => del(x)

print("--------------------")


