import matplotlib.pyplot as plt
import numpy as np

# Revisar esto: PySpark Development - Ramón Rubio Hortelano
# Regresión polinomica
# overfitting teniendo un error cuadrático (square error)

np.random.seed(2)

# Draw random samples from a normal (Gaussian) distribution
x = np.random.normal(3.0, 1.0, 1000)
print("np.random.normal(3.0, 1.0, 1000):\n", x)

y = np.random.normal(50.0, 10.0, 1000) / x
print("np.random.normal(50.0, 10.0, 1000) / x:\n", y)

plt.scatter(x, y)
#plt.show()

# probando con una regresión líneal

from scipy import stats

slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
print("Rcuadrado: ", r_value**2)
print("slope: ", slope)
print("intercept: ", intercept)

ecuacionLineal=lambda x:slope*x+intercept
predictedAmount=ecuacionLineal(x)
plt.plot(x, predictedAmount, c='r')
plt.show()