"""
@author: Fabrizio Romano
transcript: SCelis

/SCProjects/0_SCProjects_github.com_SCelisV$ python3 python/SC.Code/learn.pp/learnpp/map.example.py

# map.example.py


los elementos de cada iterable se aplican a la función; 
al principio el primer elemento de cada iterable, 
luego el segundo de cada iterable, y así sucesivamente. 

map se detiene cuando se agota el más corto de los iterables con los que lo hemos llamado
NO es obligatorio a nivelar todos los iterables a una longitud común común, 
y no se rompe si no tienen la misma longitud.
"""

"""
1 iterable
no podemos ver el objeto
>>> map(lambda *a: a, range(3))
<map object at 0x7fcebe8db2e0>

para ver el objeto utilizamos el alias que hemos creado _ = list
>>> _(map(lambda *a: a, range(3)))
[(0,), (1,), (2,)]

"""
_ = list

print( _(map(lambda *a: a, range(3))) )


"""
2 iterables
no podemos ver el objeto
>>> map(lambda *a: a, range(3), 'abc')
<map object at 0x7fcebe8db2e0>

para ver el objeto utilizamos el alias que hemos creado _ = list
>>> _(map(lambda *a: a, range(3), 'abc'))
[(0, 'a'), (1, 'b'), (2, 'c')]

"""

print(_(map(lambda *a: a, range(3), 'abc')))

"""
3 iterables
no podemos ver el objeto
>>> map(lambda *a: a, range(3), 'abc', range(4, 7))
<map object at 0x7fcebe7a3be0>

para ver el objeto utilizamos el alias que hemos creado _ = list
>>> _(map(lambda *a: a, range(3), 'abc', range(4, 7)))
[(0, 'a', 4), (1, 'b', 5), (2, 'c', 6)]
"""

print(_(map(lambda *a: a, range(3), 'abc', range(4, 7))))

"""
map stops at the shortest iterator - empty tuple is shortest
no podemos ver el objeto
>>> map(lambda *a: a, (), 'abc')
<map object at 0x7fcebe8db2e0>

para ver el objeto utilizamos el alias que hemos creado _ = list
>>> _(map(lambda *a: a, (), 'abc'))
[]
"""

print(_(map(lambda *a: a, (), 'abc')))

"""
map stops at the shortest iterator - (1, 2) shortest
no podemos ver el objeto
>>> map(lambda *a: a, (1, 2), 'abc')
<map object at 0x7fcebe7f95b0>

para ver el objeto utilizamos el alias que hemos creado _ = list
>>> _(map(lambda *a: a, (1, 2), 'abc'))
[(1, 'a'), (2, 'b')]


"""

print(_(map(lambda *a: a, (1, 2), 'abc')))


"""
map stops at the shortest iterator - (1, 2) shortest
no podemos ver el objeto
>>> map(lambda *a: a, (1, 2, 3, 4), 'abc')
<map object at 0x7fcebe8db0d0>

para ver el objeto utilizamos el alias que hemos creado _ = list
>>> _(map(lambda *a: a, (1, 2, 3, 4), 'abc'))
[(1, 'a'), (2, 'b'), (3, 'c')]

"""
print(_(map(lambda *a: a, (1, 2), 'abc')))

