from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
from pylab import randn
"""
Identificar puntos atípicos ó outlayers fuera del Bigote - ROBUSTA
"""
X = randn(500)
plt.boxplot(X)
plt.boxplot(X, notch=bool)
plt.savefig("/home/hadoop/SCProjects/0_SCProjects_github.com_SCelisV/python/SC.Code/pue-cca175/pictures/figura13_boxplot.png", format="png")
plt.show()

