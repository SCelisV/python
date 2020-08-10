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

# Traceback (most recent call last):
#   File "tuplas.py", line 17, in <module>
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

