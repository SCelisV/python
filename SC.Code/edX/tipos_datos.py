# cadena de caracteres - Strings
cadena = "Esto es una cadena de caracteres"
tipo_cadena = type(cadena)
print(tipo_cadena)
print("Hello world")
print('Hello World')
print('''Hello World''')
print("""Hello World""")
print(type("Hello world"))
print(type('Hello World'))
print(type('''Hello World'''))
print(type("""Hello World"""))
#  -O-J-O- Ejecución 
# <type 'str'>
# Hello world
# Hello World
# Hello World
# Hello World
# <class 'str'>
# <class 'str'>
# <class 'str'>
# <class 'str'>

print("Bye" + "World")
#  -O-J-O- Ejecución 
# ByeWorld


# número entero
entero = 42
tipo_entero = type(entero)
print(tipo_entero)

#  -O-J-O- Ejecución 
# <type 'int'>

# número con decimales
flotante = 42.42
tipo_flotante = type(flotante)
print(tipo_flotante)
#  -O-J-O- Ejecución 
# <type 'float'>


# Boolean
boolTrue = True
boolFalse = False
tipo_booleanT = type(boolTrue)
tipo_booleanF = type(boolFalse)

print(boolTrue, boolFalse)
print(tipo_booleanT, tipo_booleanF)

#  -O-J-O- Ejecución 
# True False
# <class 'bool'> <class 'bool'>


# lista - se pueden modificar
print('Listas - se pueden modificar')
lista = [1,2,3,4,5,1,2,3,4,5]
tipo_lista = type(lista)
print(tipo_lista)
ListStrings = ['Hello', 'Bye', 'Adios']
ListEnteros = [10, 20, 30]
ListCombinada = [10, 'Hello', True, 10.01]
print(ListStrings)
print(ListEnteros)
print(ListCombinada)
print(type(ListStrings))
print(type(ListEnteros))
print(type(ListCombinada))
print(type([1,2]))
#  -O-J-O- Ejecución 
# Listas - se pueden modificar
# <type 'list'>
# ['Hello', 'Bye', 'Adios']
# [10, 20, 30]
# [10, 'Hello', True, 10.01]
# <class 'list'>
# <class 'list'>
# <class 'list'>
# <class 'list'>

# Tuplas
# Es una lista que no se puede modificar - Inmutable
print('Tuplas: es una lista que no se puede modificar - Inmutable')
Meses = ('Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre')
print(Meses)
print(type(Meses))
print(type((1,80)))
#  -O-J-O- Ejecución 
# Listas - se pueden modificar
# ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')
# <class 'tuple'>
# <class 'tuple'>

# Dictionaries - JSON - un tipo de dato por entidad
print("Dictionaries - JSON - key-value")
Person={"FirstName":"Ryan",
"LastName":"Ray",
"NickName":"Fazt"}
print(Person)
print(type(Person))
Position={"Latitud" : 40, "Longitud" : 50}
print(type(Position))

#  -O-J-O- Ejecución
# Dictionaries - JSON - key-value
# {'FirstName': 'Ryan', 'LastName': 'Ray', 'NickName': 'Fazt'}
# <class 'dict'>
# <class 'dict'>

# None

None
print(None, "es un tipo de dato que no tiene nada, asignar un tipo de dato a un objeto")
print(type(None))

#  -O-J-O- Ejecución
# None
# <class 'NoneType'>