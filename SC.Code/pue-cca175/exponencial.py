import numpy as np
import matplotlib.pyplot as plt

# Exponencial
from scipy.stats import expon

x = np.arange(0, 10.0, 0.001)
plt.plot(x, expon.pdf(x))   #
plt.show()

# Binomial
from scipy.stats import binom

n, p = 10, 0.5
x = np.arange(0, 10.0, 0.001)
plt.plot(x, binom.pmf(x, n, p)) # funcion de probabilidad binomial
plt.show()

# POISSON
from scipy.stats import poisson

mu = 500
v = np.arange(400, 600, 0.5)
plt.plot(v, poisson.pmf(v, mu))     # funcion de densidad
plt.show()

