
"""
https://numpy.org/doc/stable/reference/generated/numpy.dot.html?highlight=dot#numpy.dot
numpy.dot(a, b, out=None)
    Dot product of two arrays. Producto punto de dos arrays
        Si a y b son matrices 1-D, es el producto interno de vectores
        Si a y b son matrices bidimensionales, es una multiplicación de matrices, pero es preferible utilizar matmul o a @ b.
        Si a o b son 0-D (escalares), es equivalente a multiplicar y se prefiere usar numpy.multiply(a, b) o a * b.
        Si a es un array N-D y b es un array 1-D, es un producto de suma sobre el último eje de a y b.
        Si a es un arreglo N-D y b es un arreglo M-D (donde M>=2), es un producto de la suma sobre el último eje de a y el penúltimo eje de b:
            dot(a, b)[i,j,k,m] = sum(a[i,j,:] * b[k,:,m])

        Devuelve error, Si la última dimensión de a no tiene el mismo tamaño que la penúltima dimensión de b.
"""
import numpy as np
x = np.array([6, 4, 8, 9, 4, 8, 10, 9, 5, 6])
y = np.array([5, 5, 7, 5, 3, 8, 10, 8, 7, 6])
print("dot(x, y): ", np.dot(x, y))
