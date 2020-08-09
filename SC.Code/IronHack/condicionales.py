entrada = raw_input("Introduce un numero entero: ")
# convertimos la cadena de caracteres en entero. Esta operacion se llama cast. 
numero = int(entrada)

# Ahora veamos que has puesto
if numero == 42: 
	print("Has elegido 42")
elif numero < 42: 
	print("El numero", numero, "es menor que 42")
else: 
	print("El numero", numero, "es mayor que 42")
#   OJO - Ejecucion
#   Introduce un numero entero: 45
# ('El numero', 45, 'es mayor que 42')

numberOne = raw_input("Introduce un numero entero: ")
numberTwo = raw_input("Introduce un numero entero: ")
a = int(numberOne)
b = int(numberTwo)

if a == b: 
	print("%d" %a, "es igual %d" %b)
elif a < b: 
	  print("el numero %d" %a, "es menor que %d" %b)
else:
	  print("el numero %d" %a, "es mayor que %d" %b)
# OJO - Ejecucion
# Introduce un numero entero: 5
# Introduce un numero entero: 5
# ('5', 'es igual 5')
# Introduce un numero entero: 2
# Introduce un numero entero: 9
# ('el numero 2', 'es menor que 9')
# Introduce un numero entero: 9
# Introduce un numero entero: 2
# ('el numero 9', 'es mayor que 2')


# A statement is evaulated as true if one of the following is correct: 
# 1. The "True" boolean variable is given, or calculated using an expression, such as an arithmetic comparison. 
# 2. An object which is not considered "empty" is passed.
# Here are some examples for objects which are considered as empty: 
# 1. An empty string: "" 
# 2. An empty list: []
# 3. The number zero: 0 
# 4. The false boolean variable: False

statement = False
another_statement = True

# O-J-O- Ejecucion:
# elif another_statement is True: 

statement = True
another_statement = False

# O-J-O- Ejecucion:
# if statement is True:

statement = False
another_statement = False

# O-J-O- Ejecucion:
# else: statement is False , another_statement is False

statement = True
another_statement = True

# O-J-O- Ejecucion:
# else: if statement is True:

if statement is True:
    # do something
    print("if statement is True: ")
elif another_statement is True: # else if
    # do something else
    print("elif another_statement is True: ")
else:
    # do another thing
    print("else: statement is False , another_statement is False")

x = 2
if x == 2:
    print("x equals two!") # O-J-O- Ejecucion: x equals two!
else:
    print("x does not equal to two.")