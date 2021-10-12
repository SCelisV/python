"""
read automoviles3.csv

write automoviles4.csv
"""

print("-------------------------------------------crear datosDF from file ---------------------------------------")
print("automoviles3.csv")

import numpy as np
import pandas as pd

# Leer archivo generado 
datosDF = pd.read_csv("/home/hadoop/0_DEVELOP__0_DEVELOP__0_DEVELOP__/Python/PycharmProjects/pythonPUE/files/automoviles3.csv")

# Revisar datos:
print("datosDF.head()\n", datosDF.head())

print(datosDF[["length", "width", "height"]].describe())
print(datosDF[["length", "width", "height"]].head())
#print("datosDF.dtypes: ", datosDF.dtypes)
print('npi de para que hace esto - ¿porcentaje sobre el total?: datosDF["length"] = datosDF["length"] / datosDF["length"].max() con length, width, heigh')

# Enfoque: reemplazo por ( valor original / valor maximo )
datosDF["length"] = datosDF["length"] / datosDF["length"].max()
datosDF["width"] = datosDF["width"] / datosDF["width"].max()
datosDF["height"] = datosDF["height"] / datosDF["height"].max()

print(datosDF[["length", "width", "height"]].head())

# Binning
datosDF["horsepower"] = datosDF["horsepower"].astype("float")

# Decision: 4 bins - cubos  = 3 visibles y el derecho funcion de corte
anchoCubos = (max(datosDF["horsepower"]) - min(datosDF["horsepower"])) / 4
print('anchoCubos: (max(datosDF["horsepower"]) - min(datosDF["horsepower"])) / 4', anchoCubos)

# Matriz de cubos (bins)
print('cubos: np.arange(min(datosDF["horsepower"]), max(datosDF["horsepower"]), anchoCubos)')
cubos = np.arange(min(datosDF["horsepower"]), max(datosDF["horsepower"]), anchoCubos)
print(cubos)

nombres_cubos = ["Bajo", "Medio", "Alto"]
print('["Bajo", "Medio", "Alto"]', nombres_cubos)

# Crear nueva columna con la funcion de corte - segmentación
"""
Clasifique los valores en intervalos discretos.
Utilice la función cortar cuando necesite segmentar y ordenar los valores de los datos en intervalos. 
Esta función también es útil para pasar de una variable continua a una variable categórica. 
Por ejemplo, cortar puede convertir las edades en grupos de intervalos de edad. 
Admite la segmentación en un número igual de intervalos, o en una matriz preestablecida de intervalos.
cubos => [ 48.  101.5 155.  208.5]
Bajo [ 48.  101.5 ]
Medio   [ 101.5 155.  ]
Alto    [ 155.  208.5]
"""
datosDF["horsepower-cubos"] = pd.cut(datosDF["horsepower"], cubos, labels=nombres_cubos, include_lowest = True)

print(datosDF[["horsepower", "horsepower-cubos"]].head(20))

print(datosDF.head())

print("-------------------------------------------Crear fichero write-----------------------------------------------")
# Grabacion del dataset en csv
datosDF.to_csv("/home/hadoop/0_DEVELOP__0_DEVELOP__0_DEVELOP__/Python/PycharmProjects/pythonPUE/files/automoviles4.csv", index = False)
