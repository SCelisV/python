import numpy as np

array_estr = np.ones(3)                                     # numpy.ones - Return a new array of given shape and type, relleno with ones.
print("array_estr: ", array_estr)                           # array_estr:  [1. 1. 1.]

array_estr = np.ones(3, dtype=([('pepe', int)]))
print("array_estr: ", array_estr)                           # array_estr:  array_estr:  [(1,) (1,) (1,)]

array_estr = np.ones(3, dtype=([('pepe', int), ('lucas', float)]))
print("array_estr: ", array_estr)                           # array_estr:  [(1, 1.) (1, 1.) (1, 1.)]

array_estr['lucas'][0] = 9.3
print("array_estr: ", array_estr)                           # array_estr:  [(1, 9.3) (1, 1. ) (1, 1. )]
print("array_estr['lucas']: ", array_estr['lucas'])         #  array_estr['lucas']:  [9.3 1.  1. ]

# Nueva vista del array con los mismos datos
array_punto = array_estr.view(np.recarray)
print("array_punto: ", array_punto)                         #   array_punto:  [(1, 9.3) (1, 1. ) (1, 1. )]
array_punto.pepe[1] = 3
print("array_punto.pepe: ", array_punto.pepe)               # array_punto.pepe:  [1 3 1]
print("array_punto.pepe[1]: ", array_punto.pepe[1])         # array_punto.pepe[1]:  3


print("array_punto.lucas: ", array_punto.lucas)             # array_punto.lucas:  [9.3 1.  1. ]
print("array_punto.lucas[2]:  ", array_punto.lucas[2])      # array_punto.lucas[2]:   1.0



