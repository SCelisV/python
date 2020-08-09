# Ejemplos de listas. 
numeros = [3,4,3,5,7,4,3,1,1]
ninjas = ['Naruto', 'Sakura', 'Sasuke', 'Hinata', 'Shikamaru']
mezcla = ['apple', 390, 876, 'orange', 'highway', 0.42, 87]

# Esto es una lista de listas que asignamos a la variable de nombre matriz
matriz = [[3,4,5], [1,2,3], [7,3,2]]

# Ejemplos de listas.
numeros = [3,4,3,5,7,4,3,1,1]
print("numeros: " + str(numeros))
# OJO - Ejecucion
# [3, 4, 3, 5, 7, 4, 3, 1, 1]

ninjas = ['Naruto', 'Sakura', 'Sasuke', 'Hinata', 'Shikamaru']
print("ninjas: " + str(ninjas))
# OJO - Ejecucion
# ['Naruto', 'Sakura', 'Sasuke', 'Hinata', 'Shikamaru']

mezcla = ['apple', 390, 876, 'orange', 'highway', 0.42, 87]
print("mezcla: " + str(mezcla))
# OJO - Ejecucion
# ['apple', 390, 876, 'orange', 'highway', 0.42, 87]

# Esto es una lista de listas que asignamos a la variable de nombre matriz
matriz = [[3,4,5], [1,2,3], [7,3,2]]
print("matriz: " + str(matriz))
print("\n")
# OJO - Ejecucion
# [[3, 4, 5], [1, 2, 3], [7, 3, 2]]

# Para seleccionar un elemento por su índice
print(ninjas[0])
print(ninjas[-1])
print(matriz[0])
# OJO - Ejecucion
# Naruto
# Shikamaru
# [3, 4, 5]

# Para seleccionar un elemento por su índice
print("ninjas[0]: " + str(ninjas[0]))
print("ninjas[-1]: " + str(ninjas[-1]))
print("matriz[0]: " + str(matriz[0]))

# OJO - Ejecucion
# ninjas[0]: Naruto
# ninjas[-1]: Shikamaru
# matriz[0]: [3, 4, 5]

# lista[start: stop: step]
print(ninjas[::2])
print(ninjas[1: 4])
print(ninjas[::-1])
# OJO - Ejecucion
# ['Naruto', 'Sasuke', 'Shikamaru']
# ['Sakura', 'Sasuke', 'Hinata']
# ['Shikamaru', 'Hinata', 'Sasuke', 'Sakura', 'Naruto']

# lista[start: stop: step]
print("step: -> ninjas[::2]: " + str(ninjas[::2]))
# OJO - Ejecucion
# step: -> ninjas[::2]: ['Naruto', 'Sasuke', 'Shikamaru']
print("\n")

print("start: stop -> ninjas[1: 4]: " + str(ninjas[1: 4]))
# OJO - Ejecucion
# start: stop -> ninjas[1: 4]: ['Sakura', 'Sasuke', 'Hinata']
print("\n")
print("start: -> ninjas[::-1]: " + str(ninjas[::-1]))
# OJO - Ejecucion
# start: -> ninjas[::-1]: ['Shikamaru', 'Hinata', 'Sasuke', 'Sakura', 'Naruto']
print("\n")
print("start: -> matriz[1:2:3]: " + str(matriz[1:2:3]))
# OJO - Ejecucion
# start: -> matriz[1:2:3]: [[1, 2, 3]]
print("\n")


# añadir un elemento nuevo al final de un lista
print(ninjas)
ninjas.append('Kakashi')
print(ninjas)
# OJO - Ejecucion
# ['Naruto', 'Sakura', 'Sasuke', 'Hinata', 'Shikamaru']['Naruto', 'Sakura', 'Sasuke', 'Hinata', 'Shikamaru', 'Kakashi']

print("\n")
print("add un elemento a la lista ninjas: ninjas.append('Kakashi'): \n" + str(ninjas))
# OJO - Ejecucion
# add un elemento a la lista ninjas: ninjas.append('Kakashi'):
# ['Naruto', 'Sakura', 'Sasuke', 'Hinata', 'Shikamaru', 'Kakashi']


# sumar listas
estudiantes = ['Harry', 'Hermione', 'Ron']
profesores = ['Dumbledore', 'Severus', 'Hagrid']
print(estudiantes)
print(profesores)
hogwards = estudiantes + profesores
print(hogwards)
# OJO - Ejecucion
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
# OJO - Ejecucion
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
# OJO - Ejecucion
# 275

# media de un conjunto de numeros
numeros = [34, 12, 93, 783, 330, 896, 1, 55]
print("numeros: \n" + str(numeros))
suma = sum(numeros)
print("sum(numeros): \n" + str(suma))
longitud = len(numeros)
print("len(numeros): \n" + str(longitud))
media = suma / longitud
print ("sum / len:\n%f") % media
# OJO - Ejecucion
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
# OJO - Ejecucion
# 1
# 896

# minimo y maximo
numeros = [34, 12, 93, 783, 330, 896, 1, 55]
# print("numeros: \n" + str(numeros))
minimo = min(numeros)
print("min(numeros): \n %d") %minimo
maximo = max(numeros)
print("max(numeros): \n %d") %maximo
# OJO - Ejecucion
# min(numeros):
#  1
# max(numeros):
#  896


# Ordenación
numeros_ordenados = sorted(numeros)
print(numeros_ordenados)
# OJO - Ejecucion
# [1, 12, 34, 55, 93, 330, 783, 896]


# Ordenacion
numeros = [34, 12, 93, 783, 330, 896, 1, 55]
# print("numeros: \n" + str(numeros))
numeros_ordenados = sorted(numeros)
print("sorted(numeros):\n " + str(numeros_ordenados))
# OJO - Ejecucion
# sorted(numeros):
#  [1, 12, 34, 55, 93, 330, 783, 896]

