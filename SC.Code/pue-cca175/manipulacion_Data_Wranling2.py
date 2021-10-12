"""
read automoviles2.csv
NaN, NAN, Not a Number
write automoviles3.csv
"""
import pandas as pd

print("-------------------------------------------crear datosDF from file ---------------------------------------")
print("automoviles2.csv")

# Leer archivo generado en Importacion.py
datosDF = pd.read_csv("/home/hadoop/0_DEVELOP__0_DEVELOP__0_DEVELOP__/Python/PycharmProjects/pythonPUE/files/automoviles2.csv")

# Revisar datos:
print("datosDF.head()\n", datosDF.head())

# 4.- Comprobar los tipos de datos de cada columna para el nuevo fichero
print('datosDF.dtypes\n', datosDF.dtypes)

# Trasposición - transposición - transponer DF:
print("datosDF.head().T\n", datosDF.head().T)

# A Float:
datosDF[["bore", "stroke", "price"]] = datosDF[["bore", "stroke", "price"]].astype("float")

# A Int:
datosDF[["normalized-losses"]] = datosDF[["normalized-losses"]].astype("int")

# 5.- Estandarizacion

# Millas por galon (mpg) cada 100 Kilometros/L = 235.2
datosDF["city-mpg"] = 235.2/datosDF["city-mpg"]

# Cambiar nombre de la columna: - rename
datosDF.rename(columns={"city-mpg" : "city-l100km"}, inplace = True)


# Millas por galon (mpg) cada 100 Kilometros/L = 235.2
datosDF["highway-mpg"] = 235.2/datosDF["highway-mpg"]

# Cambiar nombre de la columna:
datosDF.rename(columns={"highway-mpg": "highway-l100km"}, inplace = True)

print(datosDF.head())

print("-------------------------------------------Crear fichero write-----------------------------------------------")
# Grabacion del dataset en csv
# Grabar los cambios: automoviles3.csv
datosDF.to_csv("/home/hadoop/0_DEVELOP__0_DEVELOP__0_DEVELOP__/Python/PycharmProjects/pythonPUE/files/automoviles3.csv", index = False)
