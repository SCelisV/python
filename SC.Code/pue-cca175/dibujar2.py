import numpy as np

import matplotlib.pyplot as plt
from scipy.stats import norm

plt.xkcd()
figura = plt.figure()
ax = figura.add_subplot(1, 1, 1)
ax.spines['right'].set_color('none')   # funciones de nivel bajo van con  _
ax.spines['top'].set_color('none')

plt.xticks([])
plt.yticks([])

ax.set_ylim([-30, 10])

datos = np.ones(100)    # 100 datos

datos[70:]  -= np.arange(30) # from 71 -= desde 0 al 29

plt.annotate("ESTE ES UN MENSAJE\nNUEVO\nTEST", xy=(70, 1), arrowprops=dict(arrowstyle='->'), xytext=(15, -10))

plt.plot(datos)

plt.xlabel('tiempo')
plt.ylabel('salud')

plt.savefig("/home/hadoop/SCProjects/0_SCProjects_github.com_SCelisV/python/SC.Code/pue-cca175/pictures/figura8.png", format="png")  # almacenar la figura en una ruta y un png

plt.show()
