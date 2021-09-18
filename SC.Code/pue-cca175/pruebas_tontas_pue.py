def mifuncion(x):
    return x + 3


x = mifuncion(3)
print(x)  # 6


def funcionChachi(f, x):
    return f(x)


# siempre return x + 3; si x = 0 entonces return 3
print(funcionChachi(mifuncion, 8))  # 11

l = [1, 2, 3]
l2 = filter(lambda n: n % 2.0 == 0, l)
print(l)  # [1, 2, 3]
print(l2)  # <filter object at 0x7fb80af4fe50>

print(dir(l))
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

def es_par(n):
    return n % 2.0 == 0


print(es_par(3))    #   False


lista = [1, 2, 3, 4, 5, 6]
print(lista)    #   [1, 2, 3, 4, 5, 6]


lista2 = [1, 'manzana', True, 4, 5, 6]
print(lista2)   #   [1, 'manzana', True, 4, 5, 6]


x = [111, 22, 33, 44, 445, 46, 98, 3]
print(x[:3])    #   [111, 22, 33]   # n primeros

print(x[3:])    #   [44, 445, 46, 98, 3]    # salta los n primeros

print(x[-2:])   #   [98, 3]     # n últimos

x.extend([9, 9])    # añade - extiende dos elementos a la lista
print(x)   #   [111, 22, 33, 44, 445, 46, 98, 3, 9, 9]

x.append(5)     # añade - append - add elemento
print(x)    #   [111, 22, 33, 44, 445, 46, 98, 3, 9, 9, 5]

print("--------------------")

y = [45, 33, 17]
metalista = [x, y]      # crea una lista de listas
print(metalista)        #   [[111, 22, 33, 44, 445, 46, 98, 3, 9, 9, 5], [45, 33, 17]]

print("--------------------")

a = [8, 11, 1]
a.sort()    #   ordena ó clasifica
print(a)    #   [1, 8, 11]

print("--------------------")

a.sort(reverse=True)    #   ordena la lista al reves
print(a)    #   [11, 8, 1]

print("--------------------")

numbers = [1, 2, 3, 4, 5, 6]
for number in numbers:
    print(number),
    if (number % 2 == 0):
        print("es par")
    else:
        print("es impar")
print("Terminado")

# slicing
# numpy_library.py:462:# slicing (cortar) in numpy arrays
# pandas_library.py:253:# You can perform slicing (cortar) using the name of the column:
# pandas_library.py:321:# You can perform slicing (cortar) using the index of the column:

# [inicio:final:skeep]

unaLista = [99, True, "frase", [2, 4]]
unaVariable = unaLista[0:2]
print(unaVariable)      #   [99, True]

unaVariable = unaLista[0:2:1]
print(unaVariable)      #   [99, True]

unaVariable = unaLista[0:1:1]
print(unaVariable)      #   [99]

unaVariable = unaLista[0:4:3]
print(unaVariable)      #   [99, [2, 4]]

def achuchar(a, b, c):
    return a, b, c


x = achuchar(1, "langosta", 8.2)
print(x)    #   (1, 'langosta', 8.2)

print(x[2])     #   8.2

a = (1, 2, 3)
b = (4, 5, 6)
listaTuplas = [a,b]
print(listaTuplas)      #       [(1, 2, 3), (4, 5, 6)]

print(dir(a))
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']

x = {"elementoUno,": 1, "elementoDos": 2, "elementoTres": 3, "elementoCuatro": 4, "elementoCinco": 5}
type(x)
print(x)    #   {'elementoUno,': 1, 'elementoDos': 2, 'elementoTres': 3, 'elementoCuatro': 4, 'elementoCinco': 5}
print(x["elementoTres"])        #       3

print(x.keys())        #    dict_keys(['elementoUno,', 'elementoDos', 'elementoTres', 'elementoCuatro', 'elementoCinco'])

print(x.values())      #    dict_values([1, 2, 3, 4, 5])

capitanes = {}
print(capitanes)    #   {}
capitanes["Enterprise"] = "Kirk"
type(capitanes)     #   <class 'dict'>
print(capitanes)    #   {'Enterprise': 'Kirk'}

capitanes["Enterprise Super"] = "Picard"
print(capitanes)    #   {'Enterprise': 'Kirk', 'Enterprise Super': 'Picard'}

print(capitanes["Enterprise"])      #   Kirk
print(capitanes.values())           #   dict_values(['Kirk', 'Picard'])

print(capitanes.get(("Voyager")))   #   None

capitanes["Voyager"] = "Jane"
print(capitanes.get(("Voyager")))   #   Jane

for nave in capitanes:
    print (nave + ": " + capitanes[nave])

# Enterprise: Kirk
# Enterprise Super: Picard
# Voyager: Jane

print(1 == 3)     #   False

print(1 == 3 or 1 == 1)    #   True

print(1 == 3 and 1 == 1)   #   False

print(2 is 3)       #       False

print(1 < 3)        #   True

print(3 >= 3)       #   True

print(not(8>6))     #   False


# print(i)        #   NameError: name 'i' is not defined
for i in range(10):
    print(i)

#   0
#   1
#   2
#   3
#   4
#   5
#   6
#   7
#   8
#   9

print(i)        #   9

for b in range(5):
    print(b)
    if (b is 1):
        continue
    if (b > 3):
        break
    print(b)

#   0
#   0
#   1
#   2
#   2
#   3
#   3
#   4

for i in range(10):
    variable = "par" if (i % 2 == 0) else "impar"
    print(variable)

#   par
#   impar
#   par
#   impar
#   par
#   impar
#   par
#   impar
#   par
#   impar

x = 0
while (x < 3):
    print(x)
    x += 1

#   0
#   1
#   2

salir = False
while not salir:
    entrada = input()
    if entrada == "adios":
        salir = True
    else:
        print(entrada)      #   lo que dijite el usuario en la entrada