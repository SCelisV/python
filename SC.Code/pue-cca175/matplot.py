import numpy as np
import matplotlib.pyplot as plt

# Si esto no funciona a la primera:
x = np.random.normal(50, 30, 10000)
plt.hist(x, 50)
plt.show()

# intentar instalar $ sudo yum install python36-tkinter
# $ yum -y install rh-python36-numpy

# Uniforme
y = np.random.uniform(-10.0, 10.0, 100000)
plt.hist(y, 50)
plt.show()

# Gaussiana - Normal
from scipy.stats import norm

z = np.arange(-3.3, 0.01)
plt.plot(z, norm.pdf(z))   # probability density function
plt.show()

mu = 5.0
sigma = 2.0
valores = np.random.normal(mu, sigma, 10000)
plt.hist(valores, 50)
plt.show()

