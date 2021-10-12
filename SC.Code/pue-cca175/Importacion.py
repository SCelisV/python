"""
DataFrame
read excel and
write csv
NaN, NAN, Not a Number
"""
import pandas as pd

# Leer archivo generado en Importacion.py
datosDF = pd.read_excel("/home/hadoop/0_DEVELOP__0_DEVELOP__0_DEVELOP__/Python/PycharmProjects/pythonPUE/files/cars.xls")

print("datosDF.head(5):\n", datosDF.head(5))
print("datosDF.tail(10):\n", datosDF.tail(10))

# Crea la cabecera
headers = ["Price", "Mileage", "Make", "Model",	"Trim",	"Type",	"Cylinder",	"Liter", "Doors", "Cruise",	"Sound", "Leather"]
# print("headers: ", headers)
# Asigna la cabecera al DF
datosDF.columns = headers

# Ver las cabeceras
print("datosDF.columns:\n", datosDF.columns)

print("datosDF.head(10):\n", datosDF.head(10))

# Omitir datos no numericos (NaN) en price
datosDF.dropna(subset=["Price"], axis=0)

print("datosDF.head(20):\n", datosDF.head(20))

# Grabacion del dataset en csv
datosDF.to_csv("/home/hadoop/0_DEVELOP__0_DEVELOP__0_DEVELOP__/Python/PycharmProjects/pythonPUE/files/cars.csv")


"""
datosDF = pd.read_csv("/home/training/Downloads/imports-85.data", header=None)
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
"drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight", "engine-type",
"num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
"peak-rpm","city-mpg","highway-mpg","price"]"""

