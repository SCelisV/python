from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

plt.rcdefaults()
values = [ 12, 55, 4, 32, 14]
colors = ['r', 'g', 'b', 'c', 'm']
explode = [0, 0, 0.2, 0, 0]
labels = ['India', 'United States', 'Rusia', 'China', 'Europe']
plt.pie(values, colors=colors, labels=labels, explode=explode)
plt.title('Nacionalidad Trabajadores')
plt.savefig("/home/hadoop/SCProjects/0_SCProjects_github.com_SCelisV/python/SC.Code/pue-cca175/pictures/figura10_tarta.png", format="png")
plt.show()
