# set.py

print("Set => coleccion desordenada SIN indice")
print("para establecer un set: => Colors = {'Red', 'Green', 'Blue'}")
Colors = {'Red', 'Green', 'Blue'}
print(f"{Colors}, es de tipo: {type(Colors)}")


# -O-J-O- Ejecución

# Set => coleccion desordenada SIN indice
# para establecer un set: => Colors = {'Red', 'Green', 'Blue'}
# {'Blue', 'Green', 'Red'}, es de tipo: <class 'set'>

print("--------------------")

# print(dir(Colors)) - métodos
# ['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 
# 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']


print("Para saber si un elemento esta en un set: => ('Red' in Colors) ó ('Violet' in Colors)")
print('Red' in Colors)
print('Violet' in Colors)

# -O-J-O- Ejecución
# Para saber si un elemento esta en un set: => ('Red' in Colors) ó ('Violet' in Colors)
# True
# False

print("--------------------")

print(f"Para adicionar un elemento a un set: => Colors.add('Violet')")
Colors.add('Violet')
print(Colors)

# -O-J-O- Ejecución

# Para adicionar un elemento a un set: => Colors.add('Violet')
# {'Blue', 'Violet', 'Red', 'Green'}

print("--------------------")

print(f"Para remover un elemento a un set: => Colors.remove('Red')")
Colors.remove('Red')
print(Colors)

# -O-J-O- Ejecución
# Para remover un elemento a un set: => Colors.remove('Red')
# {'Blue', 'Green', 'Violet'}

print("--------------------")

print(f"Para borrar el set: => Colors.clear())")
Colors.clear()
print(Colors)


# -O-J-O- Ejecución
# Para borrar el set: => Colors.clear())
# set()

print("--------------------")

print(f"Para eliminar el set: => del Colors")
del Colors

# - O-J-O- Genera el siguiente error: - 

# print(Colors)

# Traceback (most recent call last):
#   File "set.py", line 70, in <module>
#     print(Colors)
# NameError: name 'Colors' is not defined

print("--------------------")