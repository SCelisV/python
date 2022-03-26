"""
@author: Fabrizio Romano
transcript: SCelis

# squares.py

# /home/hadoop/SCProjects/0_SCProjects_github.com_SCelisV/python/SC.Code/learn.pp/learnpp/

├── func_from.py
├── func_import.py
├── lib
   ├── funcdef.py
   └── __init__.py

"""

# squaring through the power operator - calcular la potencia de un número implica una multiplicación.., por tanto,
# cualquier algoritmo que se utilice para realizar la operación de potencia, 
# no es probable que supere a una simple multiplicación

def square1(n):
    return n ** 2

# squaring through multiplication - ligeramente más rápida
def square2(n):
    return n * n