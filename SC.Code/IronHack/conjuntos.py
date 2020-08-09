# lista con valores repetidos
lista_peliculas_cine = ['Alien', 'Terminator 2', 'Arma Letal', 'Alien', 'Terminator 2']

# conjunto con los valores de la lista sin repetir
opciones_peliculas = set(lista_peliculas_cine)

print(lista_peliculas_cine)
print(opciones_peliculas)
# OJO - Ejecucion
# ['Alien', 'Terminator 2', 'Arma Letal', 'Alien', 'Terminator 2']
# set(['Alien', 'Terminator 2', 'Arma Letal'])

# lista con valores repetidos
lista = ['Alien', 'Terminator 2', 'Arma Letal', 'Alien', 'Terminator 2']
print("lista --> repetidos: \n" + str(lista))

# conjunto con los valores de la lista sin repetir
conjunto = set(lista)
print("conjunto, no repetidos --> set(lista):\n" + str(conjunto))
# OJO - Ejecucion
# lista --> repetidos:
# ['Alien', 'Terminator 2', 'Arma Letal', 'Alien', 'Terminator 2']
# conjunto, no repetidos --> set(lista):
# set(['Alien', 'Terminator 2', 'Arma Letal'])