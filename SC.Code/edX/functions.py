# functions.py - How do define functions in Python? and How do you call functions in Python

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

# -O-J-O- Ejecución

# 40
# 610

# print(add())

# - O-J-O- Genera el siguiente error: - 
# Traceback (most recent call last):
#   File "functions.py", line 42, in <module>
#     print(add())
# TypeError: add() missing 2 required positional arguments: 'numberOne' and 'numberTwo'

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

def my_function():
    print("Hello From My Function!")

my_function()

# -O-J-O- Ejecución
# Hello From My Function!

print("--------------------")

def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))

my_function_with_args("John Doe", "a great year!")

# -O-J-O- Ejecución
# Hello, John Doe , From My Function!, I wish you a great year!

print("--------------------")

def sum_two_numbers(a, b):
    return a + b

x = sum_two_numbers(1,2)
print (x)

# -O-J-O- Ejecución
# 3

print("--------------------")

###############
#  Excercise  #
###############

# Add a function named list_benefits() that returns the following list of strings: 
# "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

def list_benefits():
    lst=["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"]
    return lst

print(list_benefits())

print("--------------------")

# -O-J-O- Ejecución
# ['More organized code', 'More readable code', 'Easier code reuse', 'Allowing programmers to share and connect code together']

def list_benefits_02():
    return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

print(list_benefits_02())

# -O-J-O- Ejecución
# ['More organized code', 'More readable code', 'Easier code reuse', 'Allowing programmers to share and connect code together']

print("--------------------")

# Add a function named build_sentence(info) which receives a single argument containing a string and 
# returns a sentence starting with the given string and ending with the string " is a benefit of functions!"

def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit

print(build_sentence("More organized code"))

# -O-J-O- Ejecución
# More organized code is a benefit of functions!

print("--------------------")

# Modify this function to concatenate to each benefit - " is a benefit of functions!"

def build_sentence_02(benefit):
    sentence = benefit + " is a benefit of functions! - concatenate"
    return sentence

print(build_sentence_02("More organized code"))

print("--------------------")

# Add a function named name_the_benefits_of_functions() which
# returns a sentence starting with the given string and ending with the string " is a benefit of functions!"

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()

# -O-J-O- Ejecución
# More organized code is a benefit of functions!
# More readable code is a benefit of functions!
# Easier code reuse is a benefit of functions!
# Allowing programmers to share and connect code together is a benefit of functions!

print("--------------------")

# Modify this function to receive a list of benefits and print it

def name_the_benefits_of_functions_02(list_of_benefits):
    for benefit in list_of_benefits:
        print(build_sentence_02(benefit))

name_the_benefits_of_functions_02(list_benefits())

# -O-J-O- Ejecución
# More organized code is a benefit of functions! - concatenate
# More readable code is a benefit of functions! - concatenate
# Easier code reuse is a benefit of functions! - concatenate
# Allowing programmers to share and connect code together is a benefit of functions! - concatenate!

print("--------------------")

def printTwice(string):
    print(f"{string}, {string}")

printTwice("esto es un string")

# -O-J-O- Ejecución
# esto es un string, esto es un string

print("--------------------")

def printTwice_02(string):
    print("%s, %s" %(string, string))

printTwice_02("esto tambien es un string")


# -O-J-O- Ejecución
# esto tambien es un string, esto tambien es un string

print("--------------------")

# Cuando creas una variable local dentro de una función, sólo existe dentro de la función, y no puedes usarla fuera.

def printLine(part1, part2):
    line = part1 + part2
    print(line)

part1 = "this is part1 "
part2 = "this is part2"
printLine(part1, part2)

# -O-J-O- Ejecución
# this is part1 this is part2

print("--------------------")

# print(line)

# - O-J-O- Genera el siguiente error: - 
# Traceback (most recent call last):
#   File "/home/hadoop/SCProjects/0_SCProjects_github.com_SCelisV/python/SC.Code/edX/functions.py", line 238, in <module>
#     print(line)
# NameError: name 'line' is not defined
print("--------------------")