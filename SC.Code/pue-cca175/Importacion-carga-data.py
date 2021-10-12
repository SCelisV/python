"""
read imports-85.data
DataFrame
read excel and
write csv
NaN, NAN, Not a Number
write automoviles1.csv
"""
import pandas as pd

datosDF = pd.read_csv("/home/hadoop/0_DEVELOP__0_DEVELOP__0_DEVELOP__/Python/PycharmProjects/pythonPUE/files/imports-85.data", header=None)

print("-------------------------------------------crear datosDF from file ---------------------------------------")
print("imports-85.data")

print("-------------------------------------------print head and tails--------------------------------------------")
print("datosDF.head(5):\n", datosDF.head(5))
print("datosDF.tail(10):\n", datosDF.tail(10))

print("-------------------------------------------Crea columns---------------------------------------------")
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
"drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight", "engine-type",
"num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
"peak-rpm","city-mpg","highway-mpg","price"]

print("-------------------------------------------Crea la cabecera y la add al DF---------------------------------------------")
datosDF.columns = headers
print("datosDF.columns = headers", datosDF.columns)
print("datosDF.head(10):\n", datosDF.head(10))

print("-------------------------------------------drop NaN-----------------------------------------------")
# Omitir datos que no numericos (NaN) en price
datosDF.dropna(subset=["price"], axis=0)
print("datosDF.head(20):\n", datosDF.head(20))

# Ver las cabeceras
print("datosDF.columns:\n", datosDF.columns)

print("-------------------------------------------Crear fichero write-----------------------------------------------")
# Grabacion del dataset en csv
datosDF.to_csv("/home/hadoop/0_DEVELOP__0_DEVELOP__0_DEVELOP__/Python/PycharmProjects/pythonPUE/files/automoviles1.csv", index = False)