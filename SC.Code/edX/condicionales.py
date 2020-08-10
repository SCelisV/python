# entrada = raw_input("Introduce un numero entero: ")
entrada = input("Introduce un numero entero: ")
# convertimos la cadena de caracteres en entero. Esta operacion se llama cast. 
numero = int(entrada)

# Ahora veamos que has puesto

if numero == 42: 
	print("Has elegido 42")
elif numero < 42: 
	print("El numero", numero, "es menor que 42")
else: 
	print("El numero", numero, "es mayor que 42")

# -O-J-O- Ejecución
#   Introduce un numero entero: 45
# ('El numero', 45, 'es mayor que 42')

print("--------------------")

# numberOne = raw_input("Introduce un numero entero: ")
numberOne = input("Introduce un numero entero: ")
# numberTwo = raw_input("Introduce un numero entero: ")
numberTwo = input("Introduce un numero entero: ")

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

print("--------------------")

# A statement is evaulated as true if one of the following is correct: 
# 1. The "True" boolean variable is given, or calculated using an expression, such as an arithmetic comparison. 
# 2. An object which is not considered "empty" is passed.

# Here are some examples for objects which are considered as empty / vacios: 
# 1. An empty string: "" 
# 2. An empty list: []
# 3. The number zero: 0 
# 4. The false boolean variable: False

string = ""
if string == "":
    print (f"if string=\"\" => preguntar por una cadena vacia => True")

lista = []
if lista == []:
    print (f"if lista == [] => preguntar por una lista vacia => True")

number = 0
if number == 0:
    print (f"if number == 0 => preguntar por el número cero => True")

boolean = False
if boolean==False:
    print (f"if boolean==False => preguntar por el boolean False => True")

# -O-J-O- Ejecución

# if string="" => preguntar por una cadena vacia => True
# if lista == [] => preguntar por una lista vacia => True
# if number == 0 => preguntar por el número cero => True
# if boolean==False => preguntar por el boolean False => True


print("--------------------")

statement = False
another_statement = True

if statement is True:
    # do something
    print(f"statement is: {statement}")
elif another_statement is True: # else if
    # do something else
    print(f"elif another_statement is: {another_statement} ")
else:
    # do another thing
    print(f"else: statement is: {statement} , another_statement is: {another_statement}")


# -O-J-O- Ejecución
# elif another_statement is: True 

print("--------------------")

statement = True
another_statement = False

if statement is True:
    # do something
    print(f"if statement is: {statement}")
elif another_statement is True: # else if
    # do something else
    print(f"elif another_statement is: {another_statement} ")
else:
    # do another thing
    print(f"else: statement is: {statement} , another_statement is: {another_statement}")

# -O-J-O- Ejecución
# if statement is: True

print("--------------------")

statement = False
another_statement = False

if statement is True:
    # do something
    print(f"if statement is: {statement}")
elif another_statement is True: # else if
    # do something else
    print(f"elif another_statement is: {another_statement} ")
else:
    # do another thing
    print(f"else: statement is: {statement} , another_statement is: {another_statement}")

# -O-J-O- Ejecución
# else: statement is: False , another_statement is: False

print("--------------------")

statement = True
another_statement = True

if statement is True:
    # do something
    print(f"if statement is: {statement}")
elif another_statement is True: # else if
    # do something else
    print(f"elif another_statement is: {another_statement} ")
else:
    # do another thing
    print(f"else: statement is: {statement} , another_statement is: {another_statement}")

# -O-J-O- Ejecución
# if statement is: True

print("--------------------")

x = 2
if x == 2:
    print("x equals two!") 
else:
    print("x does not equal to two.")

# -O-J-O- Ejecución 
# x equals two!

x = 10
x = 30

if x < 20:
    print(f"{x} is less than 20") 
else:
    print(f"{x} is grather than 20")

# -O-J-O- Ejecución , depende del valor de x

# 10 i less than 20 
# 30 is grather than 20

print("--------------------")

color = "blue"
color = "red"
color = "green"

if color == "red":
    print(f"the color is {color}")
elif color == "blue":
    print(f"the color is {color}")
else:
    print(f"any color")

# -O-J-O- Ejecución , depende del valor de color
# the color is blue
# the color is red
# any color

print("--------------------")

name = "Sonia"
lastname = "Celis"
age = 48

if name == "Sonia":
    if lastname == "Celis":
        if age == 52:
                    print(f"ok, you are {name} {lastname}")
                    print(f"ok, really you are {name}")
        elif age < 50:
                    print(f"ok, no mientas, tienes algunos más que: {age}")
        else:
            print(f"uhmm , Que dices.. algunos menos que: {age}")
    else:
        print(f":X who are you?")
else:
    print(f":/ you are not {name}")

# -O-J-O- Ejecución , depende de los valores name y lastname
# ok, you are Sonia Celis
# :X who are you?
# :/ you are not Sonia
# ok, no mientas, tienes algunos más que: 48

print("--------------------")

if x > 2 and x <= 10:
    print(f"{x} is greater than two AND less than or equal to ten ")
if x > 2 or x <= 10:
    print(f"{x} is greater than two OR less than or equal to ten ")
    if (not(x==10)):
        print(f"{x} is NOT equal 10")

# -O-J-O- Ejecución 

# 30 is greater than two OR less than or equal to ten 
# 30 is NOT equal 10

print("--------------------")

