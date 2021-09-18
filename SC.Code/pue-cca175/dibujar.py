import numpy as np

import matplotlib.pyplot as plt
# figura 7 - comic - borrador
plt.xkcd()
x = np.arange(-3, 3, 0.0001)


from scipy.stats import norm

# cambiando los  ejes
ejes = plt.axes()

# figura2
ejes.set_xlim([-5, 5])  # el eje x irá de -5, 5
ejes.set_ylim([-0, 1.0])  # el eje y irá de -0, 1.0

# figura3
ejes.set_xticks([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])  # aumenta las marcas en el eje x
ejes.set_yticks([-0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])  # aumenta las marcas en el eje y

# figura4 - grid
ejes.grid()

# general
# plt.plot(x, norm.pdf(x))
# plt.plot(x, norm.pdf(x, 1.0, 0.5))

# figura 5 - colores, y linea
plt.plot(x, norm.pdf(x), 'b-')
plt.plot(x, norm.pdf(x, 1.0, 0.5), 'r--')
# plt.plot(x, norm.pdf(x, 1.0, 0.5), 'r--') ó rD ó r. ó probar ó r:
#
# (r.. dibujar encima creo) - averiguar

# figura6 - leyenda, títulos - localización cento

plt.legend(["Azules", "Rojos"], loc=0)
# loc=9, centro, loc=0 esquina sup dcha, loc=0 esquina sup dcha, loc=2 esquina sup izq )
plt.savefig("/home/hadoop/SCProjects/0_SCProjects_github.com_SCelisV/python/SC.Code/pue-cca175/pictures/figura7.png",
            format="png")  # almacenar la figura en una ruta y un png

plt.show()
