"""
DataFrame
read excel and
write csv
NaN, NAN, Not a Number
"""
import pandas as pd

# Leer archivo generado en Importacion.py
datosDF = pd.read_excel("/home/hadoop/0_DEVELOP__0_DEVELOP__0_DEVELOP__/Python/PycharmProjects/pythonPUE/files/cars.xls")

print("----------------------------------------------------------------")
# comprobar el tipo de datos del DataFrame
print("datosDF.dtypes:\n", datosDF.dtypes)

print("----------------------------------------------------------------")
print("datosDF['Mileage']:\n", datosDF["Mileage"])

print("----------------------------------------------------------------")
# obtener un resumen estadistico del DataFrame
print("datosDF.describe(include='all'):\n", datosDF.describe(include="all"))

print("----------------------------------------------------------------")
# obtener estadiscas por columnas del DataFrame
print("datosDF[['Doors']].describe():\n", datosDF[["Doors"]].describe())
print("datosDF[['Model']].describe():\n", datosDF[["Model"]].describe())
print("datosDF[['Doors', 'Model']].describe():\n", datosDF[["Doors", "Model"]].describe())


print("----------------------------------------------------------------")
# informacion del DataFrame con Pandas
print("datosDF.info:\n", datosDF.info)

print("----------------------------------------------------------------")
print("datosDF.head(5):\n", datosDF.head(5))
print("datosDF.tail(10):\n", datosDF.tail(10))

print("----------------------------------------------------------------")
# Crea la cabecera
headers = ["Price", "Mileage", "Make", "Model",	"Trim",	"Type",	"Cylinder",	"Liter", "Doors", "Cruise",	"Sound", "Leather"]
# print("headers: ", headers)
# Asigna la cabecera al DF
datosDF.columns = headers
print("----------------------------------------------------------------")

# Ver las cabeceras
print("datosDF.columns:\n", datosDF.columns)

print("----------------------------------------------------------------")
print("datosDF.head(10):\n", datosDF.head(10))

print("----------------------------------------------------------------")
# Omitir datos no numericos (NaN) en price
datosDF.dropna(subset=["Price"], axis=0)
print("datosDF.head(20):\n", datosDF.head(20))

print("----------------------------------------------------------------")
# Grabacion del dataset en csv
datosDF.to_csv("/home/hadoop/0_DEVELOP__0_DEVELOP__0_DEVELOP__/Python/PycharmProjects/pythonPUE/files/cars.csv")