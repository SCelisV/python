# https://docs.python.org/3/tutorial/introduction.html#
# Python is completely object oriented, and not "statically typed". 
# You do not need to declare variables before using them, or declare their type. 
# Every variable in Python is an object.

# Numbers

# Python supports two types of numbers - integers and floating point numbers. 
# (It also supports complex numbers, which will not be explained in this tutorial).

# To define an integer, use the following syntax:

myint = 7
print(myint)
print("myint: " + str(myint))

# To define a floating point number, you may use one of the following notations:

myfloat = 11,5
print(myfloat)
print("myfloat: " + str(myfloat))

myfloat1 = float(myint)
print("myfloat1: " + str(myfloat1))

myfloat = 7.0
print(myfloat)

myfloat = float(7)
print(myfloat)

# Strings

# Strings are defined either with a single quote or a double quotes.

mystring = 'hello'
print(mystring)
print("mystring: " + mystring)

mystring = "Don't worry about apostrophes"
print(mystring)
print("mystring: " + mystring)

# There are additional variations on defining strings that make it easier to include things such as carriage returns, backslashes and Unicode characters. 
# These are beyond the scope of this tutorial, but are covered in the Python documentation.

# Simple operators can be executed on numbers and strings: https://docs.python.org/3/tutorial/introduction.html#strings

one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

# Assignments can be done on more than one variable "simultaneously" on the same line like this
a, b = 3.5 , 4.0
print(a,b)

c, d = 5 , 6
print(c,d)

e, f = 7, 8.5
print(e, f)

#some type of variables
mystring = "hello"
myfloat = 11,5
myint = 20


###############
#  Excercise  #
###############

# The target of this exercise is to create a string, an integer, and a floating point number. 
# The string should be named mystring and should contain the word "hello". 
# The floating point number should be named myfloat and should contain the number 10.0, and the integer should be named myint and should contain the number 20.

# change this code
mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
#The isinstance() function checks if the object (first argument) is an instance or subclass of classinfo class (second argument).
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)

#  -O-J-O- Ejecución

    # String: hello
    # Float: 10.000000
    # Integer: 20

# Example about variable definitions:

name = "SCelis"
apell = None
print("este print va después de la definición de las variables")
print(f"nombre: {name}, apellido: {apell}" )

#  -O-J-O- Ejecución
# este print va después de la definición de las variables
# nombre: SCelis, apellido: None

x, book = 100, "I Robot"
print(f"x: {x}, book: {book}")

#  -O-J-O- Ejecución
# x: 100, book: I Robot

# Conventions

book_name = "I Robot" #Snake Case
bookName = "Digital fortress" #Camel Case
BookName = "El juego de EllioT" #Pascal Case

print("Snake Case: book_name")
print("Camel Case: bookName")
print("Pascal Case: BookName")

#  -O-J-O- Ejecución
# Snake Case: book_name
# Camel Case: bookName
# Pascal Case: BookName

# CONSTANTES - CONS
PI = 3.1416
MY_NAME = "Sonia Celis"
print(PI, MY_NAME)
#  -O-J-O- Ejecución
# 3.1416 Sonia Celis

# ---------------------------------------

# Mixing operators between numbers and strings is not supported:
# This will not work!
one = 1
two = 2
hello = "hello"

print(one + two + hello)

#  -O-J-O- Ejecución Genera el siguiente error: - 

# Traceback (most recent call last):
#   File "variables.py", line 150, in <module>
#     print(one + two + hello)
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

#############
#Here are some basic argument specifiers you should know:
# %s - String (or any object with a string representation, like numbers)

# %d - Integers

# %f - Floating point numbers

# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

# %x/%X - Integers in hex representation (lowercase/uppercase)

#############

