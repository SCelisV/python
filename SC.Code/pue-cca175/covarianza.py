import numpy as np
from pylab import *

"""
buscando un ejemplo manualmente - calculo de la cov(x,y) = 2.8399999999999963
x = (6, 4, 8, 9, 4, 8, 10, 9, 5, 6)
y = (5, 5, 7, 5, 3, 8, 10, 8, 7, 6)
z = x*y
z = (30, 20, 56, 45, 12, 64, 100, 72, 35, 36)
n = 10
(sum(z)/n - (np.mean(x) * np.mean(y)) )
2.8399999999999963
"""


def d_mean(x):
    xmean = mean(x)
    return [xi - xmean for xi in x]  # calcula la diferencia de cada xi - la media de x (xi - media)


def covarianza(x, y):
    n = len(x)
    return dot(d_mean(x), d_mean(y)) / (n - 1)  # numpy.dot(a, b, out=None) # producto de dos array's

def covarianza2(x, y):
    n = len(x)
    return dot(d_mean(x), d_mean(y)) / (n)      #  numpy.dot(a, b, out=None) # producto de dos array's

x = np.array([6, 4, 8, 9, 4, 8, 10, 9, 5, 6])
print("type(x): ", type(x), " x: ", (x))        #   type(x):  <class 'numpy.ndarray'>  x:  [6  4  8  9  4  8 10  9  5  6]
y = np.array([5, 5, 7, 5, 3, 8, 10, 8, 7, 6])
print("type(y): ", type(y), " y: ", (y))        #   type(y):  <class 'numpy.ndarray'>  y:  [ 5  5  7  5  3  8 10  8  7  6]
z = x * y
print("type(z): ", type(z), " z: ", (z))        # type(z):  <class 'numpy.ndarray'>  z:  [30  20  56  45  12  64 100  72  35  36]

print(sum(x))  # 69
print(sum(y))  # 64
print(mean(x))  # 6.9
print(mean(y))  # 6.4

print("type(d_mean(x): ", type(d_mean(x)), " d_mean(x): ", d_mean(x))
print("type(d_mean(y): ", type(d_mean(y)), " d_mean(y): ", d_mean(y))
"""
type(d_mean(x):  <class 'list'>  d_mean(x):  [-0.9000000000000004, -2.9000000000000004, 1.0999999999999996, 2.0999999999999996, -2.9000000000000004, 1.0999999999999996, 3.0999999999999996, 2.0999999999999996, -1.9000000000000004, -0.9000000000000004]
type(d_mean(y):  <class 'list'>  d_mean(y):  [-1.4000000000000004, -1.4000000000000004, 0.5999999999999996, -1.4000000000000004, -3.4000000000000004, 1.5999999999999996, 3.5999999999999996, 1.5999999999999996, 0.5999999999999996, -0.40000000000000036]
"""

print("covarianza: dot(d_mean(x), d_mean(y)) / (n - 1) : ", covarianza(x, y))   # 3.1555555555555554

print("covarianza2: dot(d_mean(x), d_mean(y)) / (n) : ", covarianza2(x, y)) #   2.84

import matplotlib.pyplot as plt
plt.scatter(x, y)
plt.savefig("/home/hadoop/SCProjects/0_SCProjects_github.com_SCelisV/python/SC.Code/pue-cca175/pictures/figura14_covarianza.png", format="png")
plt.show()
