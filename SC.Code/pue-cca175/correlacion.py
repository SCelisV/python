import numpy as np
from pylab import *

def d_mean(x):
    xmean = mean(x)
    return [xi - xmean for xi in x]  # calcula la diferencia de cada xi - la media de x (xi - media)


def covarianza(x, y):
    n = len(x)
    return dot(d_mean(x), d_mean(y)) / (n-1)        #  numpy.dot(a, b, out=None) # producto de dos array's

def correlacion(x,y):
    xstd = x.std()              #   desviación standard
    ystd = y.std()
    return covarianza(x, y) / (xstd * ystd)

# 2 variables relacionadas covarianza mayor
x = np.random.normal(3.0, 1.0, 1000)
print("type(x): ", type(x))
y = np.random.normal(50.0, 10.0, 1000) / x              # los datos de x afectan la generación de los datos de y covarianza >
print("type(y): ", type(y))
"""
type(x):  <class 'numpy.ndarray'>
type(y):  <class 'numpy.ndarray'>
"""
print("covarianza: dot(d_mean(x), d_mean(y)) / (n - 1): ", covarianza(x, y))   #   covarianza: dot(d_mean(x), d_mean(y)) / (n - 1):  -1.194812502310424
print("correlacion: covarianza(x, y) / (xstd * ystd): ", correlacion(x, y))   #   correlacion: covarianza(x, y) / (xstd * ystd):  -0.020216178425236413

import matplotlib.pyplot as plt
plt.scatter(x, y)
plt.scatter(x, y, marker="1")
plt.savefig("/home/hadoop/SCProjects/0_SCProjects_github.com_SCelisV/python/SC.Code/pue-cca175/pictures/figura16_correlacion.png", format="png")
plt.show()


