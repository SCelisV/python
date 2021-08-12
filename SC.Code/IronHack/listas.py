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

# Traceback (most recent call last):
#   File "listas.py", line 255, in <module>
#     colors.extend('white', 'black', 'yellow')
# TypeError: extend() takes exactly one argument (3 given)

# - O-J-O- Genera el siguiente error: - 

# colors.append('yellow', 'black')

# Traceback (most recent call last):
#   File "listas.py", line 263, in <module>
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

# Traceback (most recent call last):
#   File "listas.py", line 320, in <module>
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
