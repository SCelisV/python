# https://docs.python.org/3/library/stdtypes.html#

x='Hello World!'
type(x)
print(x[-6])                                     # W

print("--------------------")

x = 'Hello'
y = "Hello"
if x == y:                                       # iguales
   print("iguales")
else:
   print("diferentes")
type (x)
type (y)

print("--------------------")

s1 = 'Hello'
s2 = 'Python programmers.'
print(s1 + s2)                                   # HelloPython programmers.
print(s1 + "" + s2)                              # HelloPython programmers.
print(s1 + " " + s2)                             # Hello Python programmers.
print(s1 + '' + s2)                              # HelloPython programmers.
print(s1 + ' ' + s2)                             # Hello Python programmers.
's1' + '' + 's2'                                 # 's1s2'
's1' + ' ' + 's2'                                # 's1 s2'

print("--------------------")

s = 'Python is easy to learn'
print(s[-5])                                     # l
print(s[-5:])                                    # learn
print(s[16:])                                    # o learn
print(s[17:])                                    # learn
print(s[-4:])                                    # earn

print("--------------------")

#first_name = input()                             # abc
#last_name = input()                              # xyz
first_name = "abc"
last_name = "xyz"
print("Hello" + " " + first_name + " " + last_name + "!" + " " + "You just delved into Python")
print("Hello" + " " + first_name + " " + last_name + "! " + "You just delved into Python")
print("Hello" + " " + first_name + " " + last_name + "!" + " You just delved into Python")
print("Hello " + first_name + " " + last_name + "!" + " " + "You just delved into Python")
                                                  # Hello abc xyz! You just delved into Python
                                                  # Hello abc xyz! You just delved into Python
                                                  # Hello abc xyz! You just delved into Python
                                                  # Hello abc xyz! You just delved into Python

print("--------------------")

print("------LISTA---------")
"""
list []
lists are ordered collection of objects
mutable
"""
 
item1 = "bread"
item2 = "pasta"
item3 = "fruits"

items = [item1, item2, item3]

print( "item1: ", item1)                         # item1:  bread
print( "item2: ", item2 )                        # item2:  pasta
print( "item3: ", item3 )                        # item3:  fruits

print( "items: ", items )                        # items:  ['bread', 'pasta', 'fruits']

print( "items[0]: ", items[0] )                  # items[0]:  bread
print( "items[2]: ", items[2] )                  # items[2]:  fruits

print( "items[0:2]: ", items[0:2] )              # items[0:2]:  ['bread', 'pasta']
print( "items[-1]: ", items[-1] )                # items[-1]:  fruits
print( "items[1:]: ", items[1:] )                # items[1:]:  ['pasta', 'fruits']

print( "items.append('mantequilla'): ", items.append('mantequilla') )                # None
print( "items: ", items )                        # items:  ['bread', 'pasta', 'fruits', 'mantequilla']

L = [10, 20, 30, 25, 32, 45, 50]
print(L)                                         # [10, 20, 30, 25, 32, 45, 50]

print("len(L): ", len(L))                        # len(L):  7

# es un elemento de una lista
print("L[0]: ", L[0])                            # L[0]:  10   
print("L[6]: ", L[6])                            # L[6]:  50  
print("L[-1]: ", L[-1])                          # L[-1]:  50    
print("L[6]: ", L[6])                            # L[6]:  50   

# es una lista de un elemento
print("L[-1:]: ", L[-1:])                        # L[-1:]:  [50]
print("a=L[-1:]")
a=L[-1:]
print("a: ", a)                                  # a:  [50]
print("type(a): ", type(a))                      # type(a):  <class 'list'>
print("len(a): ", len(a))                        # len(a):  1

# es una lista de un elemento
print("L[6:]: ", L[6:])                          # L[6:]:  [50]
print("a=L[6:]")
a=L[6:]
print("type(a): ", type(a))                      # type(a):  <class 'list'>
print("len(a): ", len(a))                        # len(a):  1

L = [10, 20, 30, 25, 32, 45, 50]
print("L: ", L)                                  # L:  [10, 20, 30, 25, 32, 45, 50]
L.append(20)                                     # To add 20 in the list 'L'
print("L: ", L)                                  # L:  [10, 20, 30, 25, 32, 45, 50, 20]
L.append(32)                                     # To add 32 in the list 'L'
print("L: ", L)                                  # L:  [10, 20, 30, 25, 32, 45, 50, 20, 32]
print("L.count(32): ", L.count(32))              # To print the occurrence of 32 in the list 'L' L.count(32):  2


apartments = [{'ID': '19665213.0', 'Overall Rating': '100.0', 'Price': 26.0},
              {'ID': '6436842.0', 'Overall Rating': '90.0', 'Price': 41.0},
              {'ID': '10559468.0', 'Overall Rating': '100.0', 'Price': 50.0},
              {'ID': '27215482.0', 'Overall Rating': '100.0', 'Price': 50.0},
              {'ID': '27287546.0', 'Overall Rating': '90.0', 'Price': 55.0}]

print("type(apartments): ", type(apartments)) # type(apartments):  <class 'list'>
print("longitud de la lista apartments:", len(apartments)) # longitud de la lista apartments: 5
print("the Overall Rating of the 4th apartment: ", apartments[3]['Overall Rating'])  # the Overall Rating of the 4th apartment.:  100.0

# List Methods
"""
para saber los métodos de las listas
>>> type(items)
<class 'list'>
>>> dir(items)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
"""
# .append()
# add values to the end of a list 

items.append("butter")
print( "items: ", items )                        # items:  ['bread', 'pasta', 'fruits', 'butter']

items.insert(1, 'milk')
print( "items: ", items )                        # items:  ['bread', 'milk', 'pasta', 'fruits', 'butter']


food = [ 'pan', 'pasta', 'frutas' ]
print( "food: ", food )                          # food:  ['pan', 'pasta', 'frutas']

bathroom = [ "gel de ducha", 'jabón']
print ( "bathroom", bathroom )                   # bathroom ['gel de ducha', 'jabón']

listaCompra = food + bathroom
print( "listaCompra", listaCompra )              # listaCompra ['pan', 'pasta', 'frutas', 'gel de ducha', 'jabón']

"""
# sumar una <list> con un <str>
# listaCompra + "cola"

Traceback (most recent call last):
    listaCompra + "cola"
TypeError: can only concatenate list (not "str") to list
"""

# determine the number of items found in the list it accepts as an argument len(listaCompra)
len(listaCompra)
print( "len(listaCompra)", len(listaCompra) )    # len(listaCompra) 5

if ( "pan" in listaCompra ):
  print( "entra por true" )                      # entra por true
else: 
  print( "entra por false" )

if ( "soap" in listaCompra ):
  print( "entra por true" )
else: 
  print( "entra por false" )                     # entra por false

print("--------------------")

# listas con diferente tipos de elementos
y = [1, "max", 1.6]
print("y: ", y)                                  # y:  [1, 'max', 1.6]
print(type(y))                                   # <class 'list'> 

# functions 
x = [1, 5, 3, 4, 8]
print ("x: ", x)                                 # x:  [1, 5, 3, 4, 8]
print("type(x) ", type(x))                       # type(x)  <class 'list'>

print("max(x): ", max(x))                        # max(x):  8
print("min(x): ", min(x))                        # min(x):  1

del(x)
print("del(x): borrar, delete, eliminar una tupla")

"""
print ("x: ", x)                                 

Traceback (most recent call last):
    print ("x: ", x)                                 
NameError: name 'x' is not defined
"""

print("--------------------")

"""
set {}
sets is unordered collection of objects
"""

fruits = { "apple", "banana", "cherry" }
print( "type(fruits): ", type(fruits) )          # type(fruits):  <class 'set'>
print( "fruits: ", fruits )                      # fruits:  {'apple', 'cherry', 'banana'}

"""
print( "fruits [1]: ", fruits[1] )               

type(fruits):  <class 'set'>
fruits:  {'apple', 'banana', 'cherry'}
Traceback (most recent call last):
    print( "fruits [1]: ", fruits[1] )               
TypeError: 'set' object is not subscriptable

"""
"""
print( "fruits (1): ", fruits(1) )               

type(fruits):  <class 'set'>
fruits:  {'cherry', 'banana', 'apple'}
Traceback (most recent call last):
    print( "fruits (1): ", fruits(1) )               
TypeError: 'set' object is not callable

"""
more_fruits = [ "orange", "mango", "grapes" ]
print( "more_fruits: ", more_fruits )            # more_fruits:  ['orange', 'mango', 'grapes']

print( "update fruits with more_fruits: ", fruits.update ( more_fruits ) )     # update fruits with more_fruits:  None
print( "fruits: ", fruits )                      # fruits:  {'cherry', 'banana', 'orange', 'mango', 'apple', 'grapes'} 

print( "fruits.remove: ", fruits.remove ( 'banana' ) )                         # fruits.remove:  None
print( "fruits: ", fruits )                      # fruits:  {'cherry', 'orange', 'mango', 'apple', 'grapes'}

fruits = {"apple", "banana", "cherry"}
print( "fruits: ", fruits )                      # fruits:  {'apple', 'banana', 'cherry'}

print( "fruits.discard( 'banana' ) ", fruits.discard("banana") )               # fruits.discard( 'banana' )  None
print( "fruits: ", fruits )                      # fruits:  {'cherry', 'apple'}

print("fruits.add('banana'): ", fruits.add("banana") )                         # fruits.add('banana'):  None
print( "fruits: ", fruits )                      # fruits:  {'banana', 'apple', 'cherry'}

print( "fruits.add('cherry'): ", fruits.add("cherry") )                        # fruits.add('cherry'):  None
print( "fruits: ", fruits )                      # fruits:  {'apple', 'banana', 'cherry'}

print("--------------------")

fruits = [ "apple", "banana", "cherry" ]
print( "type(fruits): ", type(fruits) )          # type(fruits):  <class 'list'>
print( "fruits: ", fruits )                      # fruits:  ['apple', 'banana', 'cherry'] 
print( "fruits [1]: ", fruits[1] )               # fruits [1]:  banana
 
print("fruits.insert(1, 'lemon'): ", fruits.insert(1, "lemon") )               # fruits.insert(1, 'lemon'):  None
print( "fruits: ", fruits )                      # fruits:  ['apple', 'lemon', 'banana', 'cherry']

print("fruits.insert(1, 'cherry'): ", fruits.insert(1, "cherry") )             # fruits.insert(1, 'cherry'):  None
print( "fruits: ", fruits )                      # fruits:  ['apple', 'cherry', 'lemon', 'banana', 'cherry']

# count()
# busca en una lista el término de búsqueda que recibe como argumento y devuelve el número de entradas coincidentes encontradas

print( "fruits.count('cherry'): ", fruits.count("cherry") )                    # fruits.count('cherry'):  2
print( "fruits: ", fruits )                      # fruits:  ['apple', 'cherry', 'lemon', 'banana', 'cherry']

numCherry = fruits.count("cherry")
print( "numCherry", numCherry )

print("--------------------")

"""
Let us say your expense for every month are listed below:

Jan - 2200
Feb - 2350
Mar - 2600
Apr - 2130
May - 2190

Create a list to store these monthly expenses and using that find out.
- In Feb, how many dollars you spent extra compare to Jan?
- Find out your total expense in first quarter (first three months) of the year.
- Find out if you spent exactly 2000 dollars in any month
- Jun month just finished and your expense is 1980 dollar.  
  Add this item to our monthly expense list
- You returned an item that you bought in a month of April and got a refund of 200$. 
  Make a correction to your monthly expense list based on this.

"""

expenses = [ 2200, 2350, 2600, 2130, 2190 ]
print( "monthly expenses: ", expenses )          # monthly expenses:  [2200, 2350, 2600, 2130, 2190]

print( "In Feb, spent: ", ( expenses[1] ) )      # In Feb, spent:  2350
print( "In Jan, spent: ", ( expenses[0] ) )      # In Jan, spent:  2200

print( "then you spent: ", ( expenses[1] - expenses[0] ), " extra in Feb" )    # then you spent:  150  extra in Feb

print( "Total expense in first quarter of year is: ", ( expenses[0] + expenses[1] + expenses[2] ) ) # Total expense in first quarter of year is:  7150

if ( 2000 in expenses ): 
  print( "there are some month where you spent exactly 2000 dollars" )
else:
  print( "there are no any month where you spent exactly 2000 dollars" )       # there are no any month where you spent exactly 2000 dollars

print( "expenses.append(1980): ", expenses.append(1980) )                      # expenses.append(1980):  None
print( "monthly expenses: ", expenses )          # monthly expenses:  [2200, 2350, 2600, 2130, 2190, 1980]

expenses[3] = expenses[3] - 200
print( "expenses[3] = expenses[3] - 200: ",  expenses[3] )                     # expenses[3] = expenses[3] - 200:  1930
print( "monthly expenses: ", expenses )          # monthly expenses:  [2200, 2350, 2600, 1930, 2190, 1980]

print("--------------------")

a = [ 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 ]
print( "a: ", a)                                 # a: [55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50] 
print( "type(a): ", type(a) )                    # type(a):  <class 'list'>
print( "len(a): ", len(a) )                      # len(a):  21

# perform the addition of a collection of numbers using the sum() function 
first=a[0:3]
print( "first=a[0:3]: " , first )                # first=a[0:3]: [55, 60, 65] 
print( "sum(first): ", sum(first) )              # sum(first):  180

second=a[3:13]
print( "second=a[3:13]: " , second )             # second=a[3:13]: [70, 75, 80, 85, 90, 95, 100, 0, 5, 10] 
print( "sum(second): ", sum(second) )            # sum(second):  610

third=a[13:]
print( "third=a[13:]: " , third )                # third=a[13:]: [15, 20, 25, 30, 35, 40, 45, 50]
print( "sum(third): ", sum(third) )              # sum(third):  260

fourth=a[-5:]
print( "fourth=a[-5:]: " , fourth )              # fourth=a[-5:]: [30, 35, 40, 45, 50] 
print( "sum(fourth): ", sum(fourth) )            # sum(fourth):  200

print("sum(a): ", sum(a))                        # sum(a): 1050

"""
ordena el contenido de cualquier lista a la que se llame. 
Las listas numéricas se ordenarán en orden ascendente, 
y las listas de cadenas se ordenarán en orden alfabético.
"""
print( "a: ", a)                                 # a:  [55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
print( "a.sort(): ", a.sort() )                  # None
print( "a: ", a)                                 # a: [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]

print("--------------------")

print("--------TUPLA-------")
"""
tupla
tuples are ordered collection of objects 
"""

"""
La tupla es también una secuencia ordenada de elementos como la lista. 
La tupla también contiene múltiples tipos de datos.
La única diferencia entre Tuple y List es que Tuple es inmutable-immutable; una vez creada no puede ser modificada.
valores separados por comas entre corchetes ()
"""

A = ('Pincel', 'Lovaina', 48851964400, 3.14, 'Mamá')
type (A)

print(A, type(A))                                # ('Pincel', 'Lovaina', 48851964400, 3.14, 'Mamá') <class 'tuple'>                

x = (1, 5, 3, 4, 8)
print ("x: ", x)                                 # x:  (1, 5, 3, 4, 8)
print(type(x))                                   # <class 'tuple'>
print("len(x): ", len(x))                        # len(x):  5
print ("x[0]: ", x[0])                           # x[0]:  1
print ("x[4]: ", x[4])                           # x[4]:  8

"""
# print ("x[5]: ", x[5])                           

Traceback (most recent call last):
    print ("x[5]: ", x[5])                           
IndexError: tuple index out of range
"""

"""
# x[0] = 2

Traceback (most recent call last):
    x[0] = 2
TypeError: 'tuple' object does not support item assignment
"""
"""
Para saber los methods permitidos en una tupla:
dir (x)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
"""
# sólo hay un número 8 en la tupla
print("x.count(8): ", x.count(8) )               # x.count(8):  1

print("len(x): ", len(x))                        # len(x):  5

# save multiple type of values
y = (1, "max", 1.6)
print("y: ", y)                                  # y:  (1, 'max', 1.6)
print(type(y))                                   # <class 'tuple'> 

# concatenar tuplas: tuple are inmutable then: you can create a new tuple 
z = x + y
print("z: ", z)                                  # z:  (1, 5, 3, 4, 8, 1, 'max', 1.6) 
print(type(z))                                   # <class 'tuple'> 

# esto creará un string NO una tupla
a = ('hi')                                       
print("a: ", a)                                  # a:  hi 
print(type(a))                                   # <class 'str'>

a = a * 5
print("a: ", a)                                  # a:  hihihihihi
print(type(a))                                   # <class 'str'>

# esto creará una tupla

b = ('hi',)                                       
print("b: ", b)                                  # b:  ('hi',)
print(type(b))                                   # <class 'tuple'>


b = b * 5
print("b: ", b)                                  # b:  ('hi', 'hi', 'hi', 'hi', 'hi')
print(type(b))                                   # <class 'tuple'>

# functions 
x = (1, 5, 3, 4, 8)
print ("x: ", x)                                 # x:  (1, 5, 3, 4, 8) 
print("type(x) ", type(x))                       # type(x)  <class 'tuple'>

print("max(x): ", max(x))                        # max(x):  8
print("min(x): ", min(x))                        # min(x):  1

print("sum(x): ", sum(x))                        # sum(x): 21

print("del(x): borrar, delete, eliminar una tupla")
del(x)

"""
print ("x: ", x)                                 

Traceback (most recent call last):
    print ("x: ", x)                               
NameError: name 'x' is not defined

"""
tup = (4, 5, 6, 7, 8)
print("tup: ",  tup)                             # tup:  (4, 5, 6, 7, 8)

"""
print("tup[8]: ", tup[8])
Traceback (most recent call last):
    print("tup[8]: ", tup[8])
IndexError: tuple index out of range

"""
tup = (4, 5, 6, 7, 8)
print("tup: ",  tup)                             # tup:  (4, 5, 6, 7, 8)

"""
print("tup[2] = 10: ", tup[2] = 10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
"""
print("tup[2]: ", tup[2])                        # tup[2]:  6

t = (4, 4, 5, 3, 4, 2, 5, 6)
print("t: ", t)                                  # t:  (4, 4, 5, 3, 4, 2, 5, 6)
print("t.count(4): ", t.count(4))                # print the number of occurrences of 4 in tuple t. t.count(4):  3º

print("--------------------")

print("-----DICTIONARY-----")
"""
dictionary {}
dictionaries are unordered collection of objects
"""
"""
(k, v)
unordered collection of key-value pairs.
contienen una lista de elementos (palabras), cada elemento tiene una clave (la palabra) y un valor (el significado de la palabra).
se utiliza cuando tenemos una gran cantidad de datos.
my_dict = {
"key1":"value1",
"key2":"value2",
}
"""
d={}
print("crear un dictionary: d={}")               # crear un dictionary: d={}
print("type(d): ", type(d))                      # type(d):  <class 'dict'>

e=dict()
print("crear un dictionary: e=dict()")           # crear un dictionary: e=dict()
print("type(e): ", type(e))                      # type(e):  <class 'dict'>

d={
# d= (k, v)
"EllioT": 13,
"George": 24,
"Sonia": 51
}
print("dictionary: d: ", d)                      # dictionary: d:  {'EllioT': 13, 'George': 24, 'Sonia': 51}


d={}
d["EllioT"] = 13
d["George"] = 24
d["Sonia"] = 51

print("dictionary: d: ", d)                      # dictionary: d:  {'EllioT': 13, 'George': (24,), 'Sonia': 51}


print("d['EllioT'] :", d['EllioT'])              # d['EllioT'] : 13

"""
Las claves de un diccionario deben ser siempre únicas e inmutables. 
The keys in a dictionary must always be unique and immutable
Esta es la razón por la que las claves del diccionario pueden ser String pero no List.
"""

"""
print("d['Lenon']: ", d['Lenon'])

Traceback (most recent call last):
    print("d['Lenon']: ", d['Lenon'])
KeyError: 'Lenon'

"""

d["Lenon"] = 13
print("d['Lenon']: ", d['Lenon'])                # d['Lenon']:  13

d["Lenon"] = 10
print("d['Lenon']: ", d['Lenon'])                # d['Lenon']:  10

d[10] = 100
print("d[10]: ", d[10])                          # d[10]:  100

"""
Iterate over key-value pairs
"""

for key, value in d.items():
    print("d[key]: ", d[key])

"""
d[key]:  13
d[key]:  24
d[key]:  51
d[key]:  10
d[key]:  100
"""

for key, value in d.items():
    print("key: ", key)
    print("value: ", value)
    print("")

"""
key:  EllioT
value:  13

key:  George
value:  24

key:  Sonia
value:  51

key:  Lenon
value:  10

key:  10
value:  100
"""
"""
los valores de un diccionario pueden ser de cualquier tipo de datos y pueden estar duplicados
las claves son sensibles a las mayúsculas y minúsculas, el mismo nombre pero diferentes casos de Clave serán tratados de forma distinta
"""

my_dict = {
  1: 'Yellow',
  2: 'Blue',
  3: 'Red',
  4: 'White'
}
print("my_dict: ", my_dict)                      # my_dict:  {1: 'Yellow', 2: 'Blue', 3: 'Red', 4: 'White'}


my_dict = {
  1: 'Yellow',
  2: 'Blue',
  3: 'Red',
  3: 'White'
}
print("my_dict: ", my_dict)                      # my_dict:  {1: 'Yellow', 2: 'Blue', 3: 'White'}

d = {"john":40, "peter":45}
print("d: ", d)                                  # d:  {'john': 40, 'peter': 45}
print("type(d): ", type(d))                      # type(d):  <class 'dict'>
d = {}
print("d: ", d)                                  # d:  {}
print("type(d): ", type(d))                      # type(d):  <class 'dict'>
d = {40:"john", 45:"peter"}
print("d: ", d)                                  # d:  {40: 'john', 45: 'peter'}
print("type(d): ", type(d))                      # type(d):  <class 'dict'>
print("len(d): ", len(d))                        # len(d):  2
"""
>>> dir (d)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

"""

print("--------------------")

print("-----FUNCTIONS------")

"""
Functions
"""

exNum1 = -5
exNum2 = 5

print("abs(exNum1): ", abs(exNum1))              # abs(exNum1):  5

if( abs(exNum1) == exNum2  ):
  print ("the numbers are the same: ", exNum1, "|", exNum2 )                   # the numbers are the same:  -5 | 5

"""
>>> help()                                     # https://docs.python.org/3.8/tutorial/.

help> quit

help> modules

help> keywords

help> symbols

help> topics

help> spam

help> modules spam

help> urllib

help> time

>>> help(str)
help> str

>>> import time

>>> help(time)
"""
exList = [5, 2, 6, 7, 8, 0]
print("max(exList): ", max(exList))              # max(exList):  8                       
print("min(exList): ", min(exList))              # min(exList):  0 

# redondea el valor decimal de un número a su número entero más cercano.
x = 5.622
print("x: ", x)                                  # x:  5.622 
print("round(x): ", round(x))                    # round(x):  6 

x = 4.622
print("x: ", x)                                  # x:  4.622
print("round(x): ", round(x))                    # round(x):  5

import math
print("math.floor(x): ", math.floor(x))          # math.floor(x):  4
print("math.ceil(x): ", math.ceil(x))            # math.ceil(x):  5              

meString = '55'
print("meString: ", meString)                    # meString:  55
print("type(meString): ", type(meString))        # type(meString):  <class 'str'>
print("cast: int(meString): ", int(meString))    # cast: int(meString):  55 
print("cast: float(meString): ", float(meString))    # cast: float(meString):  55.0 

meString = 55
print("meString: ", meString)                    # meString:  55
print("type(meString): ", type(meString))        # type(meString):  <class 'int'>
print("cast: str(meString): ", str(meString))    # cast: str(meString):  55

meString = 'hi'
print("meString: ", meString)                    # meString:  hi 
print("type(meString): ", type(meString))        # type(meString):  <class 'str'>

"""
print("cast: int(meString): ", int(meString)) 

Traceback (most recent call last):
  File "SC.Code/DPhi/basic.py", line 685, in <module>
    print("cast: int(meString): ", int(meString)) 
ValueError: invalid literal for int() with base 10: 'hi'
"""

"""
print("int('hi'): ", int('hi'))

Traceback (most recent call last):
    print("int('hi'): ", int('hi'))
ValueError: invalid literal for int() with base 10: 'hi'

"""

x = [5, 2, 6, 7, 8, 0]
print("x:", x)                                   # x: [5, 2, 6, 7, 8, 0]
print("max(x): ", max(x))                        # max(x):  8          
print("min(x): ", min(x))                        # min(x):  0          
print("len(x): ", len(x))                        # len(x):  6                                               
print("sorted(x): ", sorted(x))                  # sorted(x):  [0, 2, 5, 6, 7, 8]
print("sorted(x, reverse=True): ", sorted(x, reverse=True))                    # sorted(x, reverse=True):  [8, 7, 6, 5, 2, 0]
print("round(1.68): ", round(1.68))              # round(1.68):  2

# se puede indicar el número de decimales al que se debe redondear el número
print("round(1.68, 1)", round(1.68, 1))          # round(1.68, 1) 1.7                      

"""
Define Functions - chunks
using the def keyword.
"""
"""
convert bitcoin into USD
"""
# definición de la función
def funcion():
    print("usar funciones is cool") 

# uso de la función
funcion()                                        # usar funciones is cool 
funcion()                                        # usar funciones is cool 
funcion()                                        # usar funciones is cool 

# pasar bitcoins a dolares
def bitcoin_to_usd(btc):
    amount = btc * 527                           # one bitcoin vale 527 usd
    print(amount)

bitcoin_to_usd(3.85)                             # 2028.95 
bitcoin_to_usd(1)                                # 527
bitcoin_to_usd(13.85)                            # 7298.95

"""
Methods
In Python, everything is an object (list, string etc). 
A method in Python is similar to function 
the only difference is 
a method is dependent on the object 
a function is independent of the object.

función. len() puede utilizarse en listas, tuplas, cadenas, diccionarios, etc. para obtener el número de elementos que contienen
append() es un método que se asocia sólo a las listas. 

Los objetos tienen varios métodos asociados (dependiendo del tipo de objeto)
"""

# un método siempre pertenece a un objeto 
print("x.index(2): ", x.index(2))                # x.index(2):  1         # .index() necesita el objeto (x) para ser aplicable 
                                                                          # mientras que una función no necesariamente.

print("x.count(1): ", x.count(1))                # x.count(1):  0

word = 'abcdef'
print("word = 'abcdef': ", word )                # word = 'abcdef':  abcdef

print("word.capitalize(): ", word.capitalize())  # word.capitalize():  Abcdef

print("word.replace('c', 'xy'): ", word.replace("c", "xy"))                    # word.replace('c', 'xy'):  abxydef

"""
Todos los métodos son funciones, ¡pero no todas las funciones son métodos!

A function looks like this: function(something)
and a method looks like this: something.method()
"""

"""
Packages in Python son una colección de múltiples archivos de Python conocidos como módulos en Python
Python tiene paquetes para los directorios y módulos para los archivos.

módulos similares en un paquete y módulos diferentes en paquetes diferentes. 
Esto hace que un proyecto (programa) sea fácil de manejar y conceptualmente claro.

Un paquete de Python puede tener subpaquetes y módulos.

cada script es un módulo que realiza una función específica. ( Podemos especificar funciones, métodos, tipos en un script. )

Para la ciencia de datos, los paquetes comúnmente utilizados son:

Numpy: Trabajar con arrays
Matplotlib: Visualización de datos
Scikit-learn: ML
"""
"""
Importing packages/modules

Un paquete de Python puede tener subpaquetes en él. 
Además, estos subpaquetes tienen algunos módulos (es decir, archivos de Python).
Cada módulo consiste en algunas funciones de Python.
Para hacer uso de estas funciones necesitamos cargar el módulo en nuestro entorno de trabajo.
Para cargar cualquier paquete o módulo utilizamos el término import seguido del nombre del módulo o del nombre del paquete.
Traducción realizada con la versión gratuita del traductor www.DeepL.com/Translator
"""
import math
print("math.sqrt(16): ", math.sqrt(16))          # math.sqrt(16):  4.0

print("math.pow(2, 4): ", math.pow(2, 4))        # math.pow(2, 4):  16.0

print("math.pi: ", math.pi)                      # math.pi:  3.141592653589793

print("math.log10(100): ", math.log10(100))      # math.log10(100):  2.0

print("math.log10(1000): ", math.log10(1000))    # math.log10(1000):  3.0

print("math.floor(2.3): ", math.floor(2.3))      # math.floor(2.3):  2

print("math.ceil(2.3): ", math.ceil(2.3))        # math.ceil(2.3):  3


# functions del paquete math
# https://docs.python.org/3/library/math.html
"""
>>> dir(math)
['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
"""

import calendar

cal = calendar.month(2021,12)
print("cal = calendar.month(2021,12) :", cal)    # cal = calendar.month(2021,12) :    December 2021
"""
Mo Tu We Th Fr Sa Su
       1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28 29 30 31

"""
# es biciesto
print("calendar.isleap(2021): ", calendar.isleap(2021))                        # calendar.isleap(2021):  False 

print("calendar.isleap(2024): ", calendar.isleap(2024))                        # calendar.isleap(2024):  True

# functions del paquete calendar
# https://docs.python.org/es/3/library/calendar.html
"""
>>> dir (calendar)
['Calendar', 'EPOCH', 'FRIDAY', 'February', 'HTMLCalendar', 'IllegalMonthError', 'IllegalWeekdayError', 'January', 'LocaleHTMLCalendar', 'LocaleTextCalendar', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'TextCalendar', 'WEDNESDAY', '_EPOCH_ORD', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_colwidth', '_locale', '_localized_day', '_localized_month', '_monthlen', '_nextmonth', '_prevmonth', '_spacing', 'c', 'calendar', 'datetime', 'day_abbr', 'day_name', 'different_locale', 'error', 'firstweekday', 'format', 'formatstring', 'isleap', 'leapdays', 'main', 'mdays', 'month', 'month_abbr', 'month_name', 'monthcalendar', 'monthrange', 'prcal', 'prmonth', 'prweek', 'repeat', 'setfirstweekday', 'sys', 'timegm', 'week', 'weekday', 'weekheader']
"""

import statistics

a = [0, 1, 1, 3, 4, 9, 15]

print("statistics.mean(a): ", statistics.mean(a))                              # statistics.mean(a):  4.714285714285714
	
# Fast, floating point arithmetic mean.
print("statistics.fmean(a): ", statistics.fmean(a))                            # statistics.fmean(a):  4.714285714285714

# Harmonic mean of data.
print("statistics.harmonic_mean(a):", statistics.harmonic_mean(a))             # statistics.harmonic_mean(a): 0

# Median (middle value) of data.
print("statistics.median(a): ", statistics.median(a))                          # statistics.median(a):  3

# Single mode (most common value) of discrete or nominal data.
print("statistics.mode(a): ", statistics.mode(a))                              # statistics.mode(a):  1

# desviacion standar	
print("statistics.stdev(a): ", statistics.stdev(a))                            # statistics.stdev(a):  5.437961803049794

# functions del paquete statistics
# https://docs.python.org/3/library/statistics.html

"""
>>> dir (statistics)
['Counter', 'Decimal', 'Fraction', 'NormalDist', 'StatisticsError', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_coerce', '_convert', '_exact_ratio', '_fail_neg', '_find_lteq', '_find_rteq', '_isfinite', '_normal_dist_inv_cdf', '_ss', '_sum', 'bisect_left', 'bisect_right', 'erf', 'exp', 'fabs', 'fmean', 'fsum', 'geometric_mean', 'groupby', 'harmonic_mean', 'hypot', 'itemgetter', 'log', 'math', 'mean', 'median', 'median_grouped', 'median_high', 'median_low', 'mode', 'multimode', 'numbers', 'pstdev', 'pvariance', 'quantiles', 'random', 'sqrt', 'stdev', 'tau', 'variance']

"""
# raw strings
print(r'C:\some\name')                           # C:\some\name

print('C:\some\name')                            #  here \n means newline!
"""
C:\some
ame
"""

"""\
span multiple lines
""" 
'''
span multiple lines
'''

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

'''
produces the following output (note that the initial newline is not included):

Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to

'''
print( 3 * 'un' + 'ium' )                        # 'unununium'

print('Py' 'thon')                               # Python

prefix = 'Py'
prefix + 'thon'                                  # 'Python'

print(prefix + 'thon')                           # Python

"""

+---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1

"""
# String are immutable
word = 'Python'
print(word)
print(word[0])                                   # character in position 0 'P' -- -0 is the same as 0,
print(word[5])                                   # character in position 5 'n'
print(word[-1])                                  # last character 'n'
print(word[-2])                                  # second-last character 'o'
print(word[-6])                                  # 'P'

# ALWAYS the start is always included, and the end always excluded.

print(word[0:2])                                 # Py - 0 (included) to 2 (excluded) 
print(word[2:5])                                 # tho - 2 (included) to 5 (excluded)


print(word[:2])                                  # from the beginning to position 2 (excluded) - 'Py'
print(word[4:])                                  # from position 4 (included) to the end - 'on'
print(word[-2:])                                 # from the second-last (included) to the end - 'on'

print(word[:2] + word[2:])                       # Python
print(word[:4] + word[4:])                       # Python

"""
# the word only has 6 characters
print(word[42])                                   
Traceback (most recent call last):
IndexError: string index out of range
"""

print(word[4:42])                                # 'on'
print(word[42:])                                 # ''

"""

"""

import numpy as np
import pylab

t = np.arange(0.0, 1.0+0.01, 0.01)
s = np.cos(2*2*np.pi*t)
pylab.plot(t,s)

pylab.xlabel('time (s)')
pylab.ylabel('voltage (mV)')
pylab.title('About as simple as it gets, folks')
pylab.grid(True)
pylab.savefig('simple_plot')
pylab.show()

"""

library = package 
collection of diferen packages

library = packages + packages + packages
packages = modules + modules + modules + modules

"""