import numpy as np
from pylab import *


# 2 variables relacionadas covarianza mayor
x = np.random.normal(3.0, 1.0, 1000)
print("type(x): ", type(x))
y = np.random.normal(50.0, 10.0, 1000) / x              # los datos de x afectan la generación de los datos de y covarianza >
print("type(y): ", type(y))
"""
type(x):  <class 'numpy.ndarray'>
type(y):  <class 'numpy.ndarray'>
"""
print("cov(x,y) ", np.cov(x, y))
"""
cov(x,y)  
[[  0.95781673  -8.55697422]
 [ -8.55697422 187.35929403]]
"""
print("np.corrcoef: ", np.corrcoef(x, y))
"""
np.corrcoef:  
[[ 1.         -0.63876541]
 [-0.63876541  1.        ]]
"""

import matplotlib.pyplot as plt
plt.scatter(x, y)
plt.savefig("/home/hadoop/SCProjects/0_SCProjects_github.com_SCelisV/python/SC.Code/pue-cca175/pictures/figura18_numpy_correlacion.py.png", format="png")
plt.show()


