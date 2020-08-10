# functions.py

def hello():
    print("Hello world")

hello()

# -O-J-O- Ejecución

# Hello world

print("--------------------")

def hello_02(name="Person"): # si no le pasas ningún párametro el default/defecto de name es "Person"
    print("Hello " + name)

hello_02("Sonia")
hello_02("Celis")
hello_02()
hello_02("EllioT")

# -O-J-O- Ejecución

# Hello Sonia
# Hello Celis
# Hello Person
# Hello EllioT

print("--------------------")
def add(numberOne, numberTwo):
    return(numberOne+numberTwo)

print(add(10,30))
print(add(600,10))
# - O-J-O- Genera el siguiente error: - 
# print(add())

# Traceback (most recent call last):
#   File "functions.py", line 36, in <module>
#     print(add())
# TypeError: add() missing 2 required positional arguments: 'numberOne' and 'numberTwo'

# -O-J-O- Ejecución

# 40
# 610


print("--------------------")

def add_02(numberOne=0, numberTwo=0): # si no le pasas ningún párametro el default/defecto numberOne=0, numberTwo=0
    return(numberOne+numberTwo)

print(add_02(10,30))
print(add_02(600,10))
print(add_02())

# -O-J-O- Ejecución

# 40
# 610
# 0

print("--------------------")

print(len("add_02")) # función len predefinida de python para contar la longitud de un string

# -O-J-O- Ejecución

# 6
print("--------------------")

# función lambda => funciones anónimas que toman un número de argumentos que sólo pueden ser escritas utilizando UNA SOLA EXPRESION

add_03 = lambda numberOne, numberTwo: numberOne + numberTwo

print(add_03(5,10))


# -O-J-O- Ejecución

# 15

print("--------------------")