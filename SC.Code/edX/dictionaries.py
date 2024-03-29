# dict = tuple(key , Value) => tupla(clave, valor)

valoraciones = {'Alien':9.5, 'Terminator 2':8.9, 'Arma Letal':7.3}

# print(dir(valoraciones)) - métodos

# ['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

print("--------------------")

# algunos metodos de diccionarios
print(valoraciones['Alien'])
print(valoraciones.keys())
print(valoraciones.values())
print(valoraciones.items())

# -O-J-O- Ejecución
# 9.5
# ['Alien', 'Terminator 2', 'Arma Letal']
# [9.5, 8.9, 7.3]
# [('Alien', 9.5), ('Terminator 2', 8.9), ('Arma Letal', 7.3)]

print("--------------------")


dic = {'Alien':9.5, 'Terminator 2':8.9, 'Arma Letal':7.3}
print("dicionario -> dic{clave:valor} \n" + str(dic))
print("\n")

# algunos metodos de dicionarios
print("dic['Alien']: \n" + str(dic['Alien']))
print("dic.keys(): \n" + str(dic.keys()))
print("dic.values(): \n" + str(dic.values()))
print("dic.items(): \n" + str(dic.items()))

# -O-J-O- Ejecución
# dicionario -> dic{clave:valor}
# {'Alien': 9.5, 'Terminator 2': 8.9, 'Arma Letal': 7.3}


# dic['Alien']:
# 9.5
# dic.keys():
# ['Alien', 'Terminator 2', 'Arma Letal']
# dic.values():
# [9.5, 8.9, 7.3]
# dic.items():
# [('Alien', 9.5), ('Terminator 2', 8.9), ('Arma Letal', 7.3)]

print("--------------------")

# Dictionaries
# similar to arrays, but works with keys and values instead indexes


phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)
# -O-J-O- Ejecución
# {'John': 938477566, 'Jack': 938377264, 'Jill': 947662781}

phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook)

# -O-J-O- Ejecución
# {'John': 938477566, 'Jack': 938377264, 'Jill': 947662781}

# Iterating over dictionaries
# Dictionaries can be iterated over, just like a list. 
# However, a dictionary, unlike a list, does not keep the order of the values stored in it. 

phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

# -O-J-O- Ejecución
# Phone number of John is 938477566
# Phone number of Jack is 938377264
# Phone number of Jill is 947662781

print("--------------------")

# Removing a value
# To remove a specified index, use either one of the following notations:

phonebook = {
   "John" : 938477566,
   "Jack" : 938377264,
   "Jill" : 947662781
}
del phonebook["John"]
print(phonebook)

# -O-J-O- Ejecución
# {'Jack': 938377264, 'Jill': 947662781}

print("--------------------")

phonebook = {
   "John" : 938477566,
   "Jack" : 938377264,
   "Jill" : 947662781
}

phonebook.pop("Jill")
print(phonebook)

# -O-J-O- Ejecución
# {'Jack': 938377264}

print("--------------------")

###############
#  Excercise  #
###############

# Add "Jake" to the phonebook with the phone number 938273443, and remove Jill from the phonebook.

phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}

phonebook["Jake"] = 938273443
print(phonebook)
phonebook.pop("Jill")
print(phonebook)

# testing code
if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")
if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")

# -O-J-O- Ejecución
# {'John': 938477566, 'Jack': 938377264, 'Jill': 947662781, 'Jake': 938273443}
# {'John': 938477566, 'Jack': 938377264, 'Jake': 938273443}
# Jake is listed in the phonebook.
# Jill is not listed in the phonebook.

print("--------------------")

# carrito de compra - 
product = {
    "name" : "book",
    "quantity" : 3,
    "price" : 4.99 
}

person = {
    "first_name" : "Sonia",
    "last_name" : "Celis"
}

print(f"definir product: {product} es de tipo: {type(product)}")
print(f"imprimir las claves de un dict: => product.keys(), {product.keys()}")
print(f"imprimir la tupla (clave, valor) de un dict: => product.items(), {product.items()}")
print(f"limpiar el dict: {person} => person.clear()")
person.clear()
print(f"person:  => {person}")
# print(f"eliminar un dict: => del person, {del person}")

# -O-J-O- Ejecución
# definir product: {'name': 'book', 'quantity': 3, 'price': 4.99} es de tipo: <class 'dict'>
# imprimir las claves de un dict: => product.keys(), dict_keys(['name', 'quantity', 'price'])
# imprimir la tupla (clave, valor) de un dict: => product.items(), dict_items([('name', 'book'), ('quantity', 3), ('price', 4.99)])
# limpiar el dict: {'first_name': 'Sonia', 'last_name': 'Celis'} => person.clear()
# person:  => {}


print("--------------------")

products = [
    {"name" : "book", "price" : 4.99},
    {"name" : "laptop", "price" : 1000.99}
]


print(f"otra forma de definir products como una lista de dictionaries: {products} es de tipo: {type(products)}")


# -O-J-O- Ejecución
# otra forma de definir products como una lista de dictionaries: [{'name': 'book', 'price': 4.99}, {'name': 'laptop', 'price': 1000.99}] es de tipo: <class 'list'>

print("--------------------")

# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IN-WORK-OUT

Created on Fri Sep 11 13:33:22 2020

@author: scelis - ¯\_(ツ)_/¯

Dictionary has keys and values 
keys = index, has addresses, don't have to be integers, UNIQUE and IMMUTABLE
that are used to access values within a dictionary, The keys can be strings
values = elements and contain information are MUTABLE and DUPLICATES, multiple keys can hold the same value.
dictionary is enclosed in curly braces {}
Each key is separated from its value by a colon ":"
Commas separate the items
dictionaries.py
"""

# Create the dictionary

Dict = {}  # Dictionary vacio
print(Dict)
type(Dict)      #   <class 'dict'>

Dict = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'): 5, (0, 1): 6}
Dict
# {'key1': 1,
#  'key2': '2',
#  'key3': [3, 3, 3],
#  'key4': (4, 4, 4),
#  'key5': 5,
#  (0, 1): 6}

# Access to the value by the key
Dict["key1"]  # 1

Dict[(0, 1)] # 6

version_peliculas_dict = {
    'Thriller': '1982',
    'Back in Black': '1980',
    'The Dark Side of the Moon': '1973',
    'The Bodyguard': '1992',
    'Bat Out of Hell': '1977',
    'Their Greatest Hits (1971-1975)': '1976',
    'Saturday Night Fever': '1977',
    'Rumours': '1977'}

type(version_peliculas_dict)  # dict

# Access to the value by the key
version_peliculas_dict['Thriller']  # '1982'

# Get all the keys in dictionary - the method keys()
version_peliculas_dict.keys()
# return a list:
# dict_keys(['Thriller', 'Back in Black', 'The Dark Side of the Moon', 'The Bodyguard', 'Bat Out of Hell', 'Their Greatest Hits (1971-1975)', 'Saturday Night Fever', 'Rumours'])

# Get all the values in dictionary - the method values()
# return a list:
version_peliculas_dict.values()
# dict_values(['1982', '1980', '1973', '1992', '1977', '1976', '1977', '1977'])

# Append, add, insert value with key into dictionary
version_peliculas_dict['Graduation'] = '2007'
version_peliculas_dict
# {'Thriller': '1982',
#  'Back in Black': '1980',
#  'The Dark Side of the Moon': '1973',
#  'The Bodyguard': '1992',
#  'Bat Out of Hell': '1977',
#  'Their Greatest Hits (1971-1975)': '1976',
#  'Saturday Night Fever': '1977',
#  'Rumours': '1977',
#  'Graduation': '2007'}

# Delete entries by key
del (version_peliculas_dict['Thriller'])
del (version_peliculas_dict['Graduation'])
version_peliculas_dict
# {'Back in Black': '1980',
#  'The Dark Side of the Moon': '1973',
#  'The Bodyguard': '1992',
#  'Bat Out of Hell': '1977',
#  'Their Greatest Hits (1971-1975)': '1976',
#  'Saturday Night Fever': '1977',
#  'Rumours': '1977'}

# We can verify "find" if an element is in the dictionary
# Verify the key is in the dictionary
print("The Bodyguard IN the dict?: ", 'The Bodyguard' in version_peliculas_dict)
# The Bodyguard IN the dict?:  True
