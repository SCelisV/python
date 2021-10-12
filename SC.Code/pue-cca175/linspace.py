"""
# Revisar esto: PySpark Development - Ramón Rubio Hortelano
Por motivos de rendimiento vamos a transformar pageSpeeds y purchaseAmount a arrays de
numpy. (la función linspace nos da un listado de números separados por la misma distancia en un
rango determinado)
"""
import numpy as np
from pylab import *
import matplotlib.pyplot as plt
from scipy import stats
np.random.seed(2)

pageSpeeds = np.random.normal(3.0, 1.0, 1000)
purchaseAmount = np.random.normal(50.0, 10.0, 1000) / pageSpeeds
#-----------------------------------------------

x = np.array(pageSpeeds)
print("np.array(pageSpeeds):\n", x)

y = np.array(purchaseAmount)
print("np.array(purchaseAmount) :\n", y)

p4 = np.poly1d(np.polyfit(x, y, 4))
print("np.poly1d(np.polyfit(x, y, 4)):\n", p4)

xp = np.linspace(0, 7, 100)
print("np.linspace(0, 7, 100):\n", xp)

plt.plot(xp, p4(xp), c='r')
scatter(x, y)
plt.show()