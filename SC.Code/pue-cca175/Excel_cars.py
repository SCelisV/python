import pandas as pd
import statsmodels.api as sm

"""
RegresionMultivariable
Revisar esto: PySpark Development - Ramón Rubio Hortelano
"""
print('--------------------crea e imprime el df ----------------------------')
# lee el fichero y lo guarda en un dataframe
df = pd.read_excel('/home/hadoop/0_DEVELOP__0_DEVELOP__0_DEVELOP__/Python/PycharmProjects/pythonPUE/files/cars.xls')
print("df:\n", df)

print('--------------------convierte de categoria a ordinal ----------------------------')

# Convierte categorica a ordinal y la adiciona al dataframe
df['Model_ord'] = pd.Categorical(df.Model).codes
print("pd.Categorical(df.Model).codes:\n", pd.Categorical(df.Model).codes)
print("df:\n", df)

# Generar un nuevo dataframe con los datos a analilzar
x = df[['Mileage', 'Model_ord', 'Doors']]
print("df[['Mileage', 'Model_ord', 'Doors']]: ", x)
y = df[['Price']]
print("df[['Price']]: ", y)

print("df:\n", df)

"""
FutureWarning: In a future version of pandas all arguments of concat except for the argument 'objs' will be keyword-only
x = pd.concat(x[::order], 1)
x = pd.concat(x[::order], 1)
print("d.concat(x[::order], 1):\n", x)"""

print('--------------------OLS (Ordinary Less Square) ----------------------------')
X1 = sm.add_constant(x)
est = sm.OLS(y, X1).fit()

print('-------------------------------(Summary)-----------------------------------')
print("est.summary():\n", est.summary())

print('-------------------------------(groupby)-----------------------------------')

"""
En realidad, podíamos imaginárnos que por ejemplo, las puertas tenían baja influencia, calculando
las medias de precios de coches con 2 y 4 puertas, vemos que son bastante parecidas:
"""

df = pd.read_excel('/home/hadoop/0_DEVELOP__0_DEVELOP__0_DEVELOP__/Python/PycharmProjects/pythonPUE/files/cars.xls')
y = df[['Price']]
print("y.groupby(df.Doors).mean():\n", y.groupby(df.Doors).mean())

"""
               Price
Doors              
2      23807.135520
4      20580.670749
"""