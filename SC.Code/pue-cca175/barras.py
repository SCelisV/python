from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

values = [12, 55, 4, 32, 14]
colors = ['r', 'g', 'b', 'c', 'm']
plt.bar(range(0, 5), values, color=colors)

plt.savefig("/home/hadoop/SCProjects/0_SCProjects_github.com_SCelisV/python/SC.Code/pue-cca175/pictures/figura11_barras.png", format="png")
plt.show()
