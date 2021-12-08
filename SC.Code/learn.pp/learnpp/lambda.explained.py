"""
@author: Fabrizio Romano
transcript: SCelis

# lambda.explained.py

Definir una lambda: 
func_name = lambda [parameter_list]: expresión

A function object is returned, which is equivalent to this: 

def func_name([parameter_list]): 
    return expression

# /home/hadoop/SCProjects/learn.pp/learnpp
"""

# example 1: adder
def adder(a, b):
    return a + b

# is equivalent to:
adder_lambda = lambda a, b: a + b

print("adder_lambda: ", adder_lambda(5, 3))
# adder_lambda:  8

print("<-------------------->")

# example 2: to uppercase
def to_upper(s):
    return s.upper()

# is equivalent to:
to_upper_lambda = lambda s: s.upper()

print("to_upper_lambda: ", to_upper_lambda('construyendo funciones lambda'))
# to_upper_lambda:  CONSTRUYENDO FUNCIONES LAMBDA
