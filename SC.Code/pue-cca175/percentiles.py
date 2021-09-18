import matplotlib.pyplot as plt
import numpy as np

valores = np.random.normal(0, 0.5, 10000)
print(valores)
"""
[-0.49875939  0.1873944   0.08813093 ... -0.52154319 -0.43975048
  0.71505557]
"""
plt.hist(valores, 50)
plt.show()

print("np.percentile(valores, 20): ", np.percentile(valores, 20))   #   -0.4251565600401101
print("np.percentile(valores, 50): ", np.percentile(valores, 50))   #   0.0018756803616267745
print("np.percentile(valores, 85): ", np.percentile(valores, 85))   #    0.5247916018333564

# Momentos

import scipy.stats as sp

valores1 = np.random.normal(10, 0.5, 100)

plt.hist(valores1, 25)
plt.savefig("/home/hadoop/SCProjects/0_SCProjects_github.com_SCelisV/python/SC.Code/pue-cca175/pictures/figura9.png", format="png")
plt.show()

print("Mediana: ", np.median(valores1))     #   Mediana:  10.033191778603891
print("Varianza: ", np.var(valores1))    #   Varianza:  0.22613718085399792
print("cola-skew: ", sp.skew(valores1))     #   cola-skew:  0.05215470960454609
print("kurtosis: ", sp.kurtosis(valores1))      #   Barriga hacia la derecha    kurtosis:  cola-skew:  -0.6287877716648405
