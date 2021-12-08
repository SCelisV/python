"""
@author: Fabrizio Romano
transcript: SCelis

# filter.regular.py

lista de todos los números hasta N que son múltiplos de cinco y filtrarlos usando la función filter, 

# /home/hadoop/SCProjects/learn.pp/learnpp

"""

# filtrar los primeros n numeros naturales, esto es un poco excessive 
def is_multiple_of_five(n):
    return not n % 5

def get_multiples_of_five(n):
    return list(filter(is_multiple_of_five, range(n)))


print(get_multiples_of_five(100)) 

"""
python3 filter.regular.py 
[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
"""
