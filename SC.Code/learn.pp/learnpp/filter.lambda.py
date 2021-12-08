"""
@author: Fabrizio Romano
transcript: SCelis

# filter.lambda.py

Pythonic form

# /home/hadoop/SCProjects/learn.pp/learnpp

La lógica es exactamente la misma pero la función de filtrado es ahora una lambda

Definir una lambda: 

func_name = lambda [parameter_list]: expresión

A function object is returned, which is equivalent to this: 

def func_name([parameter_list]): 
    return expression

"""

def get_multiples_of_five(n):
    return list(filter(lambda k: not k % 5, range(n)))

print(get_multiples_of_five(100)) 

"""
$ python3 filter.lambda.py 
[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
"""