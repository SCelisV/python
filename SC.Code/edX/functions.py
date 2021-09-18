"""
IN-WORK-OUT
@author: scelis - ¯\_(ツ)_/¯

http://www.astro.up.pt/~sousasag/Python_For_Astronomers/Python_qr.pdf


functions.py
"""


# functions.py - How do define functions in Python? and How do you call functions in Python
# is a reusable block of code which performs operations specified in the function. 

# Pre-defined functions
# User defined functions

# Here are simple rules to define a function in Python:

# Functions blocks begin def followed by the function name and parentheses ().
# There are input parameters or arguments that should be placed within these parentheses.
# You can also define parameters inside these parentheses.
# There is a body within every function that starts with a colon (:) and is indented.
# You can also place documentation before the body
# The statement return exits a function, optionally passing back a value

# If there is no return statement, the function returns None. 


def hello():
    print("Hello world")


hello()

# -O-J-O- Ejecución

# Hello world

print("--------------------")


# The following two functions are equivalent:


def MJ():
    print('Michael Jackson')


def MJ1():
    print('Michael Jackson')
    return None


# None is the default return statement, See what functions returns are


print(MJ())
# Michael Jackson
# None
print(MJ1())
# Michael Jackson
# None

print("--------------------")


# return is useful when you want your output to be dependent on some condition


def type_of_album(artist, album, year_released):
    print(artist, album, year_released)
    if year_released > 1980:
        return "Modern"
    else:
        return "Oldie"


x = type_of_album("Michael Jackson", "Thriller", 1980)

print(x)

print("--------------------")


def type_of_album(y):
    """
    Recibe una tupla 

    Parameters
    ----------
    y : tuple
        artist, 
        album, 
        year_released.

    Returns
    -------
    str
        Modern or Oldier
    """

    print(y)
    if y[2] > 1980:
        return "Modern"
    else:
        return "Oldie"


y = ("Michael Jackson", "Thriller", 1980)

print(type_of_album(y))

print("--------------------")

# Add 1 to a and store as b
print("define the function: def add(a) ")


def add(a):
    """
    Parameters
    ----------
    a : int
        crea la variable b, que suma 1 a la variable a

    Returns
    -------
    b

    """
    b = a + 1
    print(a, "if you add one", b)
    return (b)


print("runing the function: add(10) ")
add(10)

help(add)  # documentation, documentación de una función """

print("--------------------")


def printStuff(Stuff):
    for i, s in enumerate(Stuff):
        print("Album", i, "Rating is ", s)


album_ratings = [10.0, 8.5, 9.5]
printStuff(album_ratings)

# Album 0 Rating is  10.0
# Album 1 Rating is  8.5
# Album 2 Rating is  9.5

print("--------------------")


def ArtistNames(*names):
    for name in names:
        print(name)


ArtistNames("Michael Jackson", "AC/DC", "Pink Floyd")

# Michael Jackson
# AC/DC
# Pink Floyd

ArtistNames("Michael Jackson", "AC/DC")

# Michael Jackson
# AC/DC

print("--------------------")


def hello_02(name="Person"):  # si no le pasas ningún párametro el default/defecto de name es "Person"
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
    return numberOne + numberTwo


print(add(10, 30))
print(add(600, 10))

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


def add_02(numberOne=0, numberTwo=0):  # si no le pasas ningún párametro el default/defecto numberOne=0, numberTwo=0
    return (numberOne + numberTwo)


print(add_02(10, 30))
print(add_02(600, 10))
print(add_02())

# -O-J-O- Ejecución

# 40
# 610
# 0

print("--------------------")

print(len("add_02"))  # función len predefinida de python para contar la longitud de un string

# -O-J-O- Ejecución

# 6

print("--------------------")

# función lambda => funciones anónimas que toman un número de argumentos que sólo pueden ser escritas utilizando UNA SOLA EXPRESION

add_03 = lambda numberOne, numberTwo: numberOne + numberTwo

print(add_03(5, 10))

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
    print("Hello, %s , From My Function!, I wish you %s" % (username, greeting))


my_function_with_args("John Doe", "a great year!")

# -O-J-O- Ejecución
# Hello, John Doe , From My Function!, I wish you a great year!

print("--------------------")


def sum_two_numbers(a, b):
    return a + b


x = sum_two_numbers(1, 2)
print(x)

# -O-J-O- Ejecución
# 3

print("--------------------")


###############
#  Excercise  #
###############

# Add a function named list_benefits() that returns the following list of strings: 
# "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

def list_benefits():
    lst = ["More organized code", "More readable code", "Easier code reuse",
           "Allowing programmers to share and connect code together"]
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
    print("%s, %s" % (string, string))


printTwice_02("esto tambien es un string")

# -O-J-O- Ejecución
# esto tambien es un string, esto tambien es un string

print("--------------------")


# inside a function is called a local variable.
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


def square(a):
    # Local variable b
    b = 1
    c = a * a + b
    print(a, "if you square + 1", c)
    return (c)


print("--------------------")


def Thriller():
    Date = 1982
    return Date


Thriller()  # 1982

Date  # Es una variable de la función por tanto ya no existe

# Traceback (most recent call last):

#   File "<ipython-input-214-25a99ea26456>", line 6, in <module>
#     Date

# NameError: name 'Date' is not defined


print("--------------------")


def ACDC(y):
    print(Rating)
    return Rating + y


Rating = 9

Z = ACDC(1)

Z  # 10

print(Rating)  # 9

print("--------------------")


# Global Scope
def PinkFloyd():
    global ClaimedSales  # the variable will be a global variable
    ClaimedSales = "45 millon"
    return ClaimedSales


PinkFloyd()  # '45 millon'

print(ClaimedSales)  # 45 millon

print("--------------------")

# Example of global variable

artist = "Michael Jackson"


def printer1(artist):
    internal_var = artist
    print(artist, "is an artist")


printer1(artist)

artist = "Michael Jackson"


# printer(internal_var)

# We got a Name Error: name 'internal_var' is not defined

def printer(artist):
    global internal_var
    internal_var = "Whitney Houston"
    print(artist, "is an artist")


printer(artist)
printer(internal_var)

print("--------------------")


# print out each element in a list:
def PrintList(the_list):
    for element in the_list:
        print(element)


PrintList(['1', 1, 'the man', "abc"])
# 1
# 1
# the man
# abc

print("--------------------")

# Scope => where the variable is accesible - Global
# outside a function definition is a global variable it's accessible and modifiable throughout the program
# After the value is returned, the scope of the function is deleted
# two ways for call a function
# Local variables only exist within the scope of a function.

# call the function with Initializes Global variable  
x = 3
# Makes function call and return function a y
y = square(x)
y

#
# 3 if you square + 1 10
# 10
#

# call the function with an input
square(3)

print("--------------------")


def AddDC(x):
    x = x + "DC"
    print(x)
    return (x)


x = "AC"
z = AddDC(x)

print("--------------------")


def recurse():
    recurse()


# recurse()

# - O-J-O- Genera el siguiente error: - 
# Traceback (most recent call last):
#   File "/Users/soniacelis/SCProjects/0_SCProjects_github.com_SCelisV/python/SC.Code/edX/functions.py", line 250, in <module>
#     recurse()
#   File "/Users/soniacelis/SCProjects/0_SCProjects_github.com_SCelisV/python/SC.Code/edX/functions.py", line 248, in recurse
#     recurse()
#   File "/Users/soniacelis/SCProjects/0_SCProjects_github.com_SCelisV/python/SC.Code/edX/functions.py", line 248, in recurse
#     recurse()
#   File "/Users/soniacelis/SCProjects/0_SCProjects_github.com_SCelisV/python/SC.Code/edX/functions.py", line 248, in recurse
#     recurse()
#   [Previous line repeated 996 more times]
# RecursionError: maximum recursion depth exceeded

print("--------------------")

# returns the area of a circle with the given radius
import math


def area(radius):
    return math.pi * radius ** 2


print("--------------------")


# to have multiple return statements, one in each branch of a conditional - debugging easier
# código muerto (lo que está después del return)  

def absoluteValue(x):
    if x < 0:
        return -x
    else:
        return x


print("--------------------")


# return la distancia entre dos puntos

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    print(f"dx is: {dx}")
    print(f"dy is: {dy}")
    dsquared = dx ** 2 + dy ** 2
    print(f"dsquared is: {dsquared}")
    result = math.sqrt(dsquared)
    return result


print("--------------------")


# Define a function for multiple two numbers

def Mult(a, b):
    c = a * b
    return (c)


Mult(2, 3)  # 6
Mult(10.0, 3.14)  # 31.400000000000002
Mult(2, "Michael Jackson ")  # 'Michael Jackson Michael Jackson '

print("--------------------")


# Define the function for combining strings
def con(a, b):
    return (a + b)


# Test on the con() function
con("This ", "is")  # 'This is'

print("--------------------")

# Pre-defined functions

# The print() function
album_ratings = [10.0, 8.5, 9.5, 7.0, 7.0, 9.5, 9.0, 9.5]
print(album_ratings)

# The sum() function -  in a list or tuple
sum(album_ratings)  # 70.0

# The len() function -  in a list or tuple
len(album_ratings)  # 8

# create a new list sorted
sorted(album_ratings)  # [7.0, 7.0, 8.5, 9.0, 9.5, 9.5, 9.5, 10.0]

# sort list no create a new list
(album_ratings).sort()

print("--------------------")


# Example for setting param with default value,
# Por ejemplo si yo quiero establecer un mínimo

def isGoodRating(rating=4):
    if (rating < 7):
        print("this album sucks it's rating is", rating)
    else:
        print("this album is good its rating is", rating)


print("--------------------")


def con(a, b):
    return (a + b)


con(['a', 1], ['b', 1])  # ['a', 1, 'b', 1]

print("--------------------")

# How do define functions in Python?

def my_function():
    print("Hello From My Function!")

def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))

def sum_two_numbers(a, b):
    return a + b

# How do you call functions in Python?
# Simply write the function's name followed by (), placing any required arguments within the brackets.

# print(a simple greeting)
my_function()

#prints - "Hello, John Doe, From My Function!, I wish you a great year!"
my_function_with_args("John Doe", "a great year!")

# after this line x will hold the value 3!
x = sum_two_numbers(1,2)
print (x)

# -O-J-O- Ejecución
# Hello From My Function!
# Hello, John Doe , From My Function!, I wish you a great year!
# 3


###############
#  Excercise  #
###############
# In this exercise you'll use an existing function, and while adding your own to create a fully functional program.

# Add a function named list_benefits() that returns the following list of strings:
# "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

# Add a function named build_sentence(info) which receives a single argument containing a string and
# returns a sentence starting with the given string and ending with the string " is a benefit of functions!"

# Run and see all the functions work together!

# # Modify this function to return a list of strings as defined above
# def list_benefits():
#     lst=["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"]
#     return lst

# # Modify this function to concatenate to each benefit - " is a benefit of functions!"
# def build_sentence(benefit):
#     sentence = benefit + " is a benefit of functions!"
#     return sentence

# def name_the_benefits_of_functions():
#     list_of_benefits = list_benefits()
#     for benefit in list_of_benefits:
#         print(build_sentence(benefit))

# name_the_benefits_of_functions()

# -O-J-O- Ejecución
# More organized code is a benefit of functions!
# More readable code is a benefit of functions!
# Easier code reuse is a benefit of functions!
# Allowing programmers to share and connect code together is a benefit of functions!

# -O-J-O- Other way

# Modify this function to return a list of strings as defined above
def list_benefits():
    return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit


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