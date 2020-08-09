# This section explains how to use basic operators in Python.

# Arithmetic Operators
# Just as any other programming languages, the addition, subtraction, multiplication, and division operators can be used with numbers.

# the order of execution in this case is: 1 + (2 * 3) / 4.0
number = 1 + 2 * 3 / 4.0
print(number)

# Try to predict what the answer will be. 
# Does python follow order of operations?

# Another operator available is the modulo (%) operator, which returns the integer remainder of the division. 
# dividend % divisor = remainder.

# O-J-O- Ejecucion remainder=2
remainder = 11 % 3
print(remainder)

# Using two multiplication symbols makes a power relationship.
squared = 7 ** 2
cubed = 2 ** 3
# O-J-O- Ejecucion raiz cuadrada - squared=49
print(squared)
# O-J-O- Ejecucion raiz cubica - cubed=8
print(cubed)

# Using Operators with Strings
# Python supports concatenating strings using the addition operator:

helloworld = "hello" + " " + "world"
print(helloworld)

# Python also supports multiplying strings to form a string with a repeating sequence:

# O-J-O- Ejecucion hellohellohellohellohellohellohellohellohellohello
lotsofhellos = "hello" * 10
print(lotsofhellos)

# Using Operators with Lists
# Lists can be joined with the addition operators:

# O-J-O- Ejecucion [1, 3, 5, 7, 2, 4, 6, 8]
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

# Just as in strings, Python supports forming new lists with a repeating sequence using the multiplication operator:
# O-J-O- Ejecucion [1, 2, 3, 1, 2, 3, 1, 2, 3]
print([1,2,3] * 3)


###############
#  Excercise  #
###############

# The target of this exercise is to create two lists called x_list and y_list, which contain 10 instances of the variables x and y, respectively. 
# You are also required to create a list called big_list, which contains the variables x and y, 10 times each, by concatenating the two lists you have created.

x = object()
y = object()

# TODO: change this code
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

x = 2
print(x == 2) # O-J-O Ejecucion: True
print(x == 3) # O-J-O Ejecucion: False
print(x < 3) # O-J-O Ejecucion: True
print(x <= 3) # O-J-O Ejecucion: True
print(x >= 3) # O-J-O Ejecucion: False
print(x != 3) # O-J-O Ejecucion: True

# Boolean operators
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
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

name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.") # O-J-O Ejecucion: Your name is either John or Rick.

# The 'is' operator
# A diferencia the double equals operator "==", the "is" operator does not match the values of the variables, but the instances themselves. 

x = [1,2,3]
y = [1,2,3]
print(x == y) # O-J-O- Ejecucion: True
print(x is y) # O-J-O- Ejecucion: False

# The "not" operator
# Using "not" before a boolean expression inverts it:

print(not False) # O-J-O- Ejecucion:  True
print((not False) == (False)) # O-J-O- Ejecucion:  False

###############
#  Excercise  #
###############

# Change the variables in the first section, so that each if statement resolves as True.

# change this code
number = 16
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print("1") # O-J-O- Ejecucion: 1

if first_array:
    print("2") # O-J-O- Ejecucion: 2

if len(second_array) == 2:
    print("3") # O-J-O- Ejecucion: 3

if len(first_array) + len(second_array) == 5:
    print("4") # O-J-O- Ejecucion: 4

if first_array and first_array[0] == 1:
    print("5") # O-J-O- Ejecucion: 5

if not second_number:
    print("6") # O-J-O- Ejecucion: 6

    