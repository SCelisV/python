import numpy as np
import numpy as np
from pylab import randn

"""
https://numpy.org/doc/stable/reference/generated/numpy.cov.html?highlight=covariance

Estimar una matriz de covarianza, dados los datos y las ponderaciones.

numpy.cov(m, y=None, rowvar=True, bias=False, ddof=None, fweights=None, aweights=None, *, dtype=None)

m: -> Cada fila de m representa una variable, y cada columna una única observación de todas esas variables

y: -> Opcional - Un conjunto adicional de variables y observaciones. tiene la misma forma que la de m

rowvar: -> True (por defecto), cada fila representa una variable, con observaciones en las columnas. 
    False, la relación se transpone: cada columna representa una variable, mientras que las filas contienen observaciones.
    
bias: Opcional -> normalización, False (por defecto) (N - 1), (estimación NO sesgada). 
    True, normalización es por N. (estimación sesgada).
    donde N es el número de observaciones dadas 
    Estos valores pueden ser anulados usando la palabra clave ddof en versiones de numpy >= 1.5
    
ddof: Opcional -> None(por defecto). Si no es así, se anula el valor por defecto implicado por el sesgo. 
     ddof=1 devolverá la estimación no sesgada, (N - 1) incluso si se especifican tanto f  como a,
     ddof=0 devolverá la media simple.
     
fweights: Opcional -> None (por defecto). Matriz 1-D de pesos de frecuencia enteros. 
                    Número de veces que debe repetirse cada vector de observación.
                    
aweights: Opcional -> None (por defecto). Matriz 1-D de pesos de vectores de observación. 
                        Estos pesos relativos suelen ser grandes para las observaciones consideradas "importantes" y más pequeños para las observaciones consideradas menos "importantes". 
            Si ddof=0, la matriz de pesos puede utilizarse para asignar probabilidades a los vectores de observación.

dtype: Opcional -> None (por defecto). Tipo de datos del resultado. 
            Por defecto, el tipo de datos devuelto tendrá al menos una precisión numpy.float64.

      
"""
# A 1-D or 2-D array

# f weights, pesos
# a weights, pesos
# m matriz de observación

# calcular la covarianza ponderada:

m = np.arange(10, dtype=np.float64)
print("m: ", m)             # m:  [0. 1. 2. 3. 4. 5. 6. 7. 8. 9.]
f = np.arange(10) * 2
print("f: ", f)             # f:  [ 0  2  4  6  8 10 12 14 16 18]
a = np.arange(10) ** 2.
print("a: ", a)             # a:  [ 0.  1.  4.  9. 16. 25. 36. 49. 64. 81.]

# ddof=1 devolverá la estimación no sesgada, (N - 1) incluso si se especifican tanto f  como a
ddof = 1

w = f * a
print("w: ", w)     #   w:  [   0.    2.   16.   54.  128.  250.  432.  686. 1024. 1458.]

v1 = np.sum(w)
print("v1: ", v1)   #   v1:  4050.0

v2 = np.sum(w * a)
print("v2: ", v2)   # v2:  241650.0

kk = m * w
print("kk: ", kk)   # kk:  [0.0000e+00 2.0000e+00 3.2000e+01 1.6200e+02 5.1200e+02 1.2500e+03 2.5920e+03 4.8020e+03 8.1920e+03 1.3122e+04]

m -= np.sum(m * w, axis=None, keepdims=True) / v1
print("m: ", m)     # m:  [-7.57185185 -6.57185185 -5.57185185 -4.57185185 -3.57185185 -2.57185185 -1.57185185 -0.57185185  0.42814815  1.42814815]

cov = np.dot(m * w, m.T) * v1 / (v1**2 - ddof * v2)
# cuando a == 1, el factor de normalización v1 / (v1**2 - ddof * v2) pasa a 1 / (np.sum(f) - ddof) como debería

print("cov: ", cov) #   cov:  2.3686219474841983

# two variables, and , which correlate perfectly, but in opposite directions

x = np.array([[0, 2], [1, 1], [2, 0]]).T        # T transpuestas
print("x: ", x)
"""
x:  
[[0 1 2]    x0 - increases
 [2 1 0]]   x1 - decreases
"""
print("cov(x): ", np.cov(x))
"""
cov(x):  
[[ 1. -1.]
 [-1.  1.]]

La relación entre x0, x1 es negativa (fila 0, columna 1) = -1

"""

x = [-2.1, -1,  4.3]
y = [3,  1.1,  0.12]
X = np.stack((x, y))    #   pila de los arrays
print("X: ", X)
"""
X:  
[[-2.1  -1.    4.3 ]
 [ 3.    1.1   0.12]]
"""
print("cov(X): ", np.cov(X))
"""
cov(X):  
[[11.71       -4.286     ]
 [-4.286       2.14413333]]
"""

X = np.stack((x, y), axis=0)
print("cov(X): ", np.cov(X))
"""
cov(X):  
[[11.71       -4.286     ]
 [-4.286       2.14413333]]
"""

x = [0, 4,  8]
y = [5, 5,  8]
X = np.stack((x, y))    #   pila de los arrays
print("X: ", X)

"""
X:  
[[0 4 8]
 [5 5 8]]
 
"""
print("cov(X): ", np.cov(X))
"""
cov(X):  
[[16.  6.]
 [ 6.  3.]]
"""
"""
buscando un ejemplo manualmente - calculo de la cov(x,y) = 2.8399999999999963
x = (6, 4, 8, 9, 4, 8, 10, 9, 5, 6)
y = (5, 5, 7, 5, 3, 8, 10, 8, 7, 6)
z = x*y
z = (30, 20, 56, 45, 12, 64, 100, 72, 35, 36)
n = 10
(sum(z)/n) - (np.mean(x) * np.mean(y))
2.8399999999999963
"""