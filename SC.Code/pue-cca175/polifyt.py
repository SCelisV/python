"""
# Revisar esto: PySpark Development - Ramón Rubio Hortelano

para este ejemplo vamos a usar polyfit, que calcula los coeficientes para un polinomio con
los puntos dados, y poly1d que nos genera el polinomio a partir de estos coeficientes.
"""

import numpy as np

x=[1,2,5,6,7,8]
y=[2,4,6,9,19,21]
pf = np.polyfit(x, y, 4)
pol = np.poly1d(pf)

print('coeficientes - pf = np.polyfit(x, y, 4): ', pf)  #   [ -0.09340219   1.69068297  -9.64511664  20.79530635 -10.83558179]
print('polinomio - pol = np.poly1d(pf):\n', pol)         #   4         3         2
"""
          4         3         2
-0.0934 x + 1.691 x - 9.645 x + 20.8 x - 10.84
"""
