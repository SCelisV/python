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
plt.show()
