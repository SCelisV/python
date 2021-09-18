from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
from pylab import randn     #   pylab is a module in matplotlib

X = randn(500)
Y = randn(500)
plt.scatter(X, Y)
plt.scatter(X, Y, marker="1")
plt.savefig("/home/hadoop/SCProjects/0_SCProjects_github.com_SCelisV/python/SC.Code/pue-cca175/pictures/figura12_scatter.png", format="png")

plt.show()

