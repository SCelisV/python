"""
IN-WORK-OUT
@author: scelis - '¯\_(ツ)_/¯'
BasicOperators.py
Version:  001
*********************
Copyright (c) 2021 - SCelis.
All Rights Reserved.
*********************
Description: This section explains how to use basic operators in Python.
*********************
ChangeLog: write me
**********
TODO:
"""
# Arithmetic Operators
# Just as any other programming languages, the addition, subtraction, multiplication, and division operators can be used with numbers.

# precedencia: PEMDAS => Parenthesis, Exponentiation, Multiplication and Division, Addition and Subtractio the order of execution in this case is: 1 + (2 * 3) / 4.0
PEMDAS = 1 + 2 * 3 / 4.0
print(PEMDAS)
print(type(PEMDAS))

# Try to predict what the answer will be.
# Does python follow order of operations?

# Another operator available is the modulo (%) operator, which returns the integer remainder of the division.
# dividend % divisor = remainder.

# -O-J-O- Ejecución remainder=2
REMAINDER = 11 % 3
print(f"remaninder: {REMAINDER}")
REMAINDER02 = 11//3
print(f"remaninder02: {REMAINDER02}")



# Using two multiplication symbols makes a power relationship.
SQUARED = 7 ** 2
CUBED = 2 ** 3
# -O-J-O- Ejecución cuadrada - squared=49
print(SQUARED)
# -O-J-O- Ejecución cubica - cubed=8
print(CUBED)

# Using Operators with Strings
# Python supports concatenating strings using the addition operator:

HELLOWORLD = "hello" + " " + "world"
print(HELLOWORLD)

# Python also supports multiplying strings to form a string with a repeating sequence:

# -O-J-O- Ejecución hellohellohellohellohellohellohellohellohellohello
LOTSOFHELLOS = "hello" * 10
print(LOTSOFHELLOS)

# Using Operators with Lists
# Lists can be joined with the addition operators:

# -O-J-O- Ejecución [1, 3, 5, 7, 2, 4, 6, 8]
EVEN_NUMBERS = [2, 4, 6, 8]
ODD_NUMBERS = [1, 3, 5, 7]
ALL_NUMBERS = ODD_NUMBERS + EVEN_NUMBERS
print(ALL_NUMBERS)

# Just as in strings, Python supports forming new lists with a repeating sequence using the multiplication operator:
# -O-J-O- Ejecución [1, 2, 3, 1, 2, 3, 1, 2, 3]
print([1, 2, 3] * 3)


###############
#  Excercise  #
###############

# The target of this exercise is to create two lists called x_list and y_list, which contain 10 instances of the variables x and y, respectively.
# You are also required to create a list called big_list, which contains the variables x and y, 10 times each, by concatenating the two lists you have created.

x = object()
y = object()

x_list = [x]*10
y_list = [y]*10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

# O-J-O Ejecucion
# x_list contains 10 objects
# y_list contains 10 objects
# big_list contains 20 objects
# Almost there...
# Great!

# Conditions

X = 2
print(X == 2) # O-J-O Ejecucion: True
print(X == 3) # O-J-O Ejecucion: False
print(X < 3) # O-J-O Ejecucion: True
print(X <= 3) # O-J-O Ejecucion: True
print(X >= 3) # O-J-O Ejecucion: False
print(X != 3) # O-J-O Ejecucion: True

# Boolean operators
NAME = "John"
AGE = 23
if NAME == "John" and AGE == 23:
    print("Your name is John, and you are also 23 years old.")

if NAME == "John" or "Rick":
    print("Your name is either John or Rick.")

# O-J-O Ejecucion:
# Your name is John, and you are also 23 years old.
# Your name is either John or Rick.


# print((5 + 5 == 10) and ('isla' != 'pantano')) : True and True
# True


# print((100 > 75) and (93 < 80)) : True and False
# False


# print((93 < 80) and (100 > 75)) : False and True
# False


# print((5 + 5 != 10) and ('isla' == 'pantano')) : False and False
# False
# -----

# print((80 < 93) or (3 in [1,2,3,4,5])) : True or True
# True


# print((100 > 75) or (93 < 80)) :  True or False
# True


# print((93 < 80) or (100 > 75)) : False or True
# True


# print((93 < 80) or (3 not in [1,2,3,4,5])) : False or False
# False

# The "in" operator could be used to check if a specified object exists within an iterable object container, such as a list:

NAME = "John"
if NAME in ["John", "Rick"]:
    print("Your name is either John or Rick.") # O-J-O Ejecucion: Your name is either John or Rick.

# The 'is' operator
# A diferencia the double equals operator "==", the "is" operator does not match the values of the variables, but the instances themselves.

x = [1, 2, 3]
y = [1, 2, 3]
print(x == y) # -O-J-O- Ejecución: True
print(x is y) # -O-J-O- Ejecución: False

# The "not" operator
# Using "not" before a boolean expression inverts it:

print(not False) # -O-J-O- Ejecución:  True
print((not False) == (False)) # -O-J-O- Ejecución:  False

###############
#  Excercise  #
###############

# Change the variables in the first section, so that each if statement resolves as True.

# change this code
NUMBER = 16
SECOND_NUMBER = 0
FIRST_ARRAY = [1, 2, 3]
SECOND_ARRAY = [1, 2]

if NUMBER > 15:
    print("1") # -O-J-O- Ejecución: 1

if FIRST_ARRAY:
    print("2") # -O-J-O- Ejecución: 2

if len(SECOND_ARRAY) == 2:
    print("3") # -O-J-O- Ejecución: 3

if len(FIRST_ARRAY) + len(SECOND_ARRAY) == 5:
    print("4") # -O-J-O- EJECUCIÓN: 4

if FIRST_ARRAY and FIRST_ARRAY[0] == 1:
    print("5") # -O-J-O- Ejecución: 5

if not SECOND_NUMBER:
    print("6") # -O-J-O- Ejecución: 6
    