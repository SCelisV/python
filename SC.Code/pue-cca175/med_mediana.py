import numpy as np
import matplotlib.pyplot as plt

"""
# numpy_library.py - for arrays and operations with arrays
https://numpy.org

"""
salarios = np.random.normal(24000, 15000, 10000)
print("salarios: ", salarios) # salarios:  [24360.89031615 25924.3157692  30725.19804873 ... 29533.74270004 19711.95061146 20048.03319674]

"""
Media - sumar todos los elementos y dividirlo por el total
"""
print("Media: ", np.mean(salarios))     #   Media:  24027.448918618677
"""
Mediana - ROBUSTA - es el valor que después de ordenar todos los valores.
- Deja la mitad de la distribución a un lado y la otra mitad al otro.
frente a los datos erroneos, esta médida no cambia. 
"""
print("Mediana: ", np.median(salarios))     #   Mediana:  23953.2646029679

salarios = np.append(salarios, [70000])
print("salarios: ", salarios) #    salarios:  [24360.89031615 25924.3157692  30725.19804873 ... 19711.95061146 20048.03319674 70000.        ]
print("Media: ", np.mean(salarios))     #   Media:  24032.04571404727
print("Mediana: ", np.median(salarios))     #   Mediana:  23954.527115765

"""
Moda - Es el valor más repetido de todos los existentes
"""
#MODA
edades = np.random.randint(18, high=90, size=500)
print("edades:", edades)

"""
edades: [22 36 83 50 44 57 69 88 38 30 86 36 35 62 30 50 59 34 68 26 62 42 20 61
 64 50 74 58 58 88 36 68 84 88 18 86 38 75 33 45 67 77 58 71 89 87 24 30
 52 24 61 88 26 79 87 46 41 45 23 64 41 78 27 34 79 73 80 69 35 41 86 87
 89 23 32 46 89 54 37 47 32 77 23 88 51 75 79 79 48 47 65 24 72 53 43 83
 54 79 34 33 41 70 28 76 44 58 58 60 64 52 66 52 20 74 31 54 42 66 55 33
 87 89 48 55 48 69 18 18 26 49 25 68 85 55 32 65 61 78 86 89 75 20 55 64
 59 62 84 53 64 32 24 53 38 27 77 39 29 22 26 76 79 86 71 44 45 88 62 77
 82 88 29 37 24 63 53 60 37 85 78 75 55 28 26 80 69 34 57 35 55 20 70 87
 29 88 23 24 18 36 31 42 28 79 63 89 86 30 47 48 68 80 39 44 80 38 55 67
 55 36 27 22 31 85 57 65 53 52 32 42 86 24 79 61 22 47 26 86 59 37 86 31
 52 53 22 52 80 34 63 41 56 41 87 50 54 32 43 74 80 49 57 56 66 79 46 86
 73 26 52 76 78 41 75 82 71 70 18 34 58 49 38 41 89 24 32 25 64 30 33 83
 21 77 32 37 80 49 38 46 67 45 33 43 88 42 63 70 77 82 20 65 34 45 68 26
 24 23 82 88 87 38 25 54 61 42 76 89 25 37 79 71 36 31 18 24 89 48 33 66
 85 33 67 46 66 43 85 60 49 72 86 54 31 26 30 23 81 81 45 66 20 62 71 87
 51 81 77 59 78 79 25 82 60 46 52 47 34 69 33 60 89 31 29 88 74 53 80 79
 59 62 44 36 58 70 53 65 69 26 22 41 55 23 79 84 40 18 79 85 37 54 57 48
 30 81 20 47 53 54 47 47 45 33 35 86 88 79 31 41 77 82 21 78 80 89 59 21
 81 65 24 86 30 62 38 78 47 29 28 45 42 52 53 37 79 76 88 39 60 47 47 28
 56 36 89 31 85 77 47 85 72 50 54 86 87 79 59 65 80 23 50 19 34 70 28 85
 62 21 46 65 37 25 20 58 73 45 81 58 43 50 23 35 88 57 59 67]
"""

from scipy import stats
moda = stats.mode(edades)
print("moda: ", moda)       #   moda:  ModeResult(mode=array([79]), count=array([17]))

print("moda: ", moda.mode, " que se repite ", moda.count, " veces.")     #  moda:  [79]  que se repite  [17]  veces.

beneficios = np.random.normal(100.0, 20.0, 10000)

plt.hist(beneficios, 50)
plt.show()
mediab = np.mean(beneficios)
medianb = np.median(beneficios)
print(mediab)
print(medianb)

