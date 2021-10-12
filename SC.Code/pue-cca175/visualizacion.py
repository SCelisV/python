"""
read automoviles4.csv

write automoviles5.csv
"""

import pandas as pd
import matplotlib as plt
from matplotlib import pyplot

# código para notebook = %matplotlib inline


print("-------------------------------------------crear datosDF from file ---------------------------------------")
print("automoviles4.csv")

datosDF = pd.read_csv("/home/hadoop/0_DEVELOP__0_DEVELOP__0_DEVELOP__/Python/PycharmProjects/pythonPUE/files/automoviles4.csv")

# Dibujar histograma para visualizar los cubos
"""
bins - int : Define el número de contenedores de igual anchura en el rango de x. 
El rango de x se amplía en un 0,1% a cada lado para incluir los valores mínimo y máximo de x.
"""
plt.pyplot.hist(datosDF["horsepower"], bins=3)
plt.pyplot.xlabel("horspower")
plt.pyplot.ylabel("contador")
plt.pyplot.title("horsepower cubos")
plt.pyplot.show()

print("datosDF.columns: \n", datosDF.columns)
print('datosDF.shape\n', datosDF.shape)

print('------------------Convertir una variable categorica en una variable ficticia / "tonta"----------------------')
# Get dummies = obtener valores numericos de una varaible categorica
print('datosDF["fuel-type"].head()\n', datosDF["fuel-type"].head())
print('pd.get_dummies(datosDF["fuel-type"]): \n')
varFiguradoDF = pd.get_dummies(datosDF["fuel-type"])
print('varFiguradoDF.head(): \n', varFiguradoDF.head())
"""
Crea dos variables - dummies - Unsigned Integers of 8 bits. 
A uint8 data type contains all whole numbers from 0 to 255.
diesel                 uint8
gas                    uint8
"""

print('------------------------------------Concat---------------------------------------------')
"""
Concatenar objetos pandas a lo largo de un eje particular con una lógica de conjunto opcional a lo largo de los otros ejes.
También puede añadir una capa de indexación jerárquica en el eje de concatenación, 
que puede ser útil si las etiquetas son las mismas (o se superponen) en el número de eje pasado.
axis{0/’index’, 1/’columns’}, default 0
"""
datosDF = pd.concat([datosDF, varFiguradoDF], axis=1)
print("pd.concat([datosDF, varFiguradoDF], axis=1)\n", datosDF.head())

print('dtypes(datosDF)\n', datosDF.dtypes)
print('datosDF.shape\n', datosDF.shape)

print('------------------------------------drop - eliminar----------------------------------')
# Decision: eliminar la columna original de fuel-type
print('datosDF.drop("fuel-type", axis=1, inplace=True)')
datosDF.drop("fuel-type", axis=1, inplace=True)
print('datosDF.shape\n', datosDF.shape)


print('--------------------dummies y concat para la variable aspiration-----------------------')
varFiguradoDF = pd.get_dummies(datosDF["aspiration"])
print(varFiguradoDF.head())

# Fusion de dataFrames
datosDF = pd.concat([datosDF, varFiguradoDF], axis=1)

# Decision: eliminar la columna original de aspiration
datosDF.drop("aspiration", axis=1, inplace=True)

print('datosDF.shape\n', datosDF.shape)

print("-----------------------------------------Crear fichero write - limpio------------------------------------------")
# Grabacion del dataset en csv
datosDF.to_csv("/home/hadoop/0_DEVELOP__0_DEVELOP__0_DEVELOP__/Python/PycharmProjects/pythonPUE/files/automoviles5.csv", index=False)

