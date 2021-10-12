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
plt.plot(x, intercept + slope * x, 'r', label='linea')
plt.legend()
plt.show()

print('Slope: ', slope, 'Intercept: ', intercept, 'r_value: ', r_value, 'p_value: ', p_value, 'str_err: ', std_err)
# Slope:  -3.0777925910974955 Intercept:  100.32883852703654 r_value:  -0.7272309406020798 p_value:  2.753085529140409e-165 str_err:  0.09195481793049737

print('Error cuadratico: ', r_value ** 2)       #   Error cuadratico:  0.5288648409689858