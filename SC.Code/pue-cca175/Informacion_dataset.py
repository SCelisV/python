"""
read automoviles1.csv
DataFrame
read excel and
write csv
NaN, NAN, Not a Number

"""
import pandas as pd

print('-----------------------------------carga lee fichero y crea DF---------------------------------------')
# Leer archivo generado en Importacion.py
datosDF = pd.read_csv("/home/hadoop/0_DEVELOP__0_DEVELOP__0_DEVELOP__/Python/PycharmProjects/pythonPUE/files/automoviles1.csv")
print("automoviles1.csv")

print('-----------------------------------types del DF---------------------------------------')
# comprobar el tipo de datos del DataFrame
print("datosDF.dtypes", datosDF.dtypes)

print("type(datosDF)\n", type(datosDF))

print('-----------------------------The column labels of the DataFrame---------------------------------------')
print('datosDF.columns\n', datosDF.columns)

print('-----------------------------------una columna del DF---------------------------------------')
print('datosDF["normalized-losses"]:\n', datosDF["normalized-losses"])


print('-----------------------------------describe DF---------------------------------------')
# obtener un resumen estadistico del DataFrame
print('datosDF.describe(include="all"):\n', datosDF.describe(include="all"))

print('--------------------------------describe de algunas columas del DF---------------------------------------')
# obtener estadiscas por columnas del DataFrame
print('datosDF[["length", "compression-ratio"]].describe()\n', datosDF[["length", "compression-ratio"]].describe())

print('-------------------------------info del DF---------------------------------------')
# informacion del DataFrame con Pandas
print("datosDF.info", datosDF.info)
