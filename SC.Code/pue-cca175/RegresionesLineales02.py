import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt

# Revisar esto: PySpark Development - Ramón Rubio Hortelano

# Regresión polinomica de orden (degree = 1).
# Draw random samples from a normal (Gaussian) distribution
x = np.random.normal(3.0, 1.0, 1000)
print("np.random.normal(3.0, 1.0, 1000):\n", x)

y = 100 - (x + np.random.normal(0, 1, 1000)) * 3
print("100 - (x + np.random.normal(0, 1, 1000)) * 3:\n", y)
plt.scatter(x, y)
plt.show()
print('---------------------------------------------------------')

from scipy import stats
from pylab import *

slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
plt.plot(x, y, 'o', label='label')
print('Error cuadratico: ', r_value ** 2)           # Error cuadratico:  0.4908670369546169
ecuacionLineal = lambda x:slope*x+intercept
predicted = ecuacionLineal(x)
plt.plot(x, predicted, c='r', label='linea')
plt.legend()
plt.show()
