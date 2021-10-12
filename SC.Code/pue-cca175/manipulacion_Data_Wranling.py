"""
read automoviles1.csv
NaN, NAN, Not a Number
write automoviles2.csv
"""
import numpy as np
import pandas as pd

print("-------------------------------------------crear datosDF from file ---------------------------------------")
print("automoviles1.csv")

# Leer archivo generado en Importacion.py
datosDF = pd.read_csv("/home/hadoop/0_DEVELOP__0_DEVELOP__0_DEVELOP__/Python/PycharmProjects/pythonPUE/files/automoviles1.csv")

print("-------------------------------------------replace NaN---------------------------------------")
# 1- convertir los "?" a NaN
print('datosDF.replace("?", np.NaN, inplace=True)', )
datosDF.replace("?", np.NaN, inplace=True)
print("datosDF.head(20)\n", datosDF.head(20))

print("-----------------------------------crea un DF con los isnull()--------------------------------")
# Evaluacion de la falta de datos en el DataFrame
print('datos_faltantesDF = datosDF.isnull()')
datos_faltantesDF = datosDF.isnull()
print('datos_faltantesDF.head(20)\n', datos_faltantesDF.head(20))

print("--------------------------contar por columnas los valores perdidos--------------------------")
"""
crea una lista con los nombres de las columnas del df
['symboling', 'normalized-losses', 'make', 'fuel-type', 'aspiration', 'num-of-doors', 'body-style', 'drive-wheels', 'engine-location', 'wheel-base', 'length', 'width', 'height', 'curb-weight', 'engine-type', 'num-of-cylinders', 'engine-size', 'fuel-system', 'bore', 'stroke', 'compression-ratio', 'horsepower', 'peak-rpm', 'city-mpg', 'highway-mpg', 'price']
"""
for columna in datos_faltantesDF.columns.values.tolist():
    print(columna)
    # value_counts(), Devuelve una serie que contiene el recuento de filas únicas en el DataFrame.
    print(datos_faltantesDF[columna].value_counts())
    print("--------------")

print("-------------------------------replace 'blancos' to NaN--------------------------------------")
# 2.- Reemplazar los valores en blanco por valores NaN - https://regexr.com/ - https://regex101.com/
print('datosDF.replace(to_replace=r"\s+", value=np.NaN, regex=True)')
print(datosDF.replace(to_replace=r"\s+", value=np.NaN, regex=True))
print('datosDF.head(20)\n', datosDF.head(20))

print("-------------------------------valores NaN (perdidos)--------------------------------------")
# 3.- Trabajar con los valores NaN (perdidos)
# 3.1.- columna: normalized-losses
# astype - Cast a pandas object to a specified dtype.
# Return the mean of the values over the requested axis.
#     axis{index (0), columns (1)}
# cambia de tipo dtype: object a tipo dtype: float64
# calcula la media sobre float
print("datosDF['normalized-losses'].astype('float').mean(axis=0)")
promedio1 = datosDF["normalized-losses"].astype("float").mean(axis=0)
print("calcula la media sobre la columna normalized-losses: ", promedio1)

# Name: normalized-losses, dtype: int64
# le cambia el tipo al promedio2 a entero
promedio2 = promedio1.astype("int")
print("promedio1.astype('int'): ", promedio2)

# sustituye los NaN por el valor de promedio2 que es de tipo entero, para no alterar el valor de la media -
datosDF["normalized-losses"].fillna(promedio2, inplace = True)
print("datosDF['normalized-losses'].fillna(promedio2, inplace = True) ")

# inplace por defecto False - Si es True, rellena en el lugar.
# Nota: esto modificará cualquier otra vista de esse objeto (por ejemplo, un corte sin copia para una columna en un DataFrame).
print(datosDF["normalized-losses"].head(5))
print(datosDF['normalized-losses'].describe())

# value_counts -  orden descendente por default
# Devuelve una serie que contiene el recuento de filas únicas en el DataFrame.
print("datosDF['normalized-losses'].value_counts()")
print("Valores de normalized-losses: ", datosDF["normalized-losses"].value_counts())

# 3.2.- columna: num-of-doors
print("Valores de num-of-doors: ", datosDF["num-of-doors"].value_counts())
# Calcular el mas comun: - Devuelve el índice de la primera aparición del máximo
print("El mas comun:\n", datosDF["num-of-doors"].value_counts().idxmax())
datosDF["num-of-doors"].fillna("four", inplace = True)
print(datosDF["num-of-doors"])

# 3.3.- columna: bore
promedio_bore = datosDF["bore"].astype("float").mean(axis=0)
print("Valor promedio de bore: ", promedio_bore)
datosDF["bore"].fillna(promedio_bore, inplace = True)
print(datosDF["bore"])

# 3.4.- columna: stroke
promedio_stroke = datosDF["stroke"].astype("float").mean(axis=0)
print("Valor promedio de stroke: ", promedio_stroke)
datosDF["stroke"].fillna(promedio_stroke, inplace= True)
print(datosDF["stroke"])

# 3.5.- columna: horsepower
promedio_horsepower = datosDF["horsepower"].astype("float").mean(axis=0)
print("Valor promedio de horsepower: ", promedio_horsepower)
datosDF["horsepower"].fillna(promedio_horsepower, inplace= True)
print(datosDF["horsepower"])

# 3.6.- columna: peak-rpm
promedio_peak_rpm = datosDF["peak-rpm"].astype("float").mean(axis=0)
print("Valor promedio de peak-rpm: ", promedio_peak_rpm)
datosDF["peak-rpm"].fillna(promedio_peak_rpm, inplace = True)
print(datosDF["peak-rpm"])

# 3.7.- columna: price
datosDF.dropna(subset=["price"], axis = 0, inplace = True)
datosDF.reset_index(drop=True, inplace = True)

print("-------------------------------valores NaN (perdidos)--------------------------------------")

# Comprobacion final:
print("datosDF.head()\n", datosDF.head())
print("datosDF.describe()\n", datosDF.describe())

print("-------------------------------------------Crear fichero write-----------------------------------------------")
# Grabacion del dataset en csv
# Grabar los cambios: automoviles2.csv
datosDF.to_csv("/home/hadoop/0_DEVELOP__0_DEVELOP__0_DEVELOP__/Python/PycharmProjects/pythonPUE/files/automoviles2.csv", index = False)
