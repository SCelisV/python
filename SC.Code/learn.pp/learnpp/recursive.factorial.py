"""
@author: Fabrizio Romano
transcript: SCelis

# recursive.factorial.py

Hay un límite, para las cantidad de llamadas anidadas

# /home/hadoop/SCProjects/learn.pp/learnpp

"""
import sys

# recursive.factorial.py
def factorial(n):
    if n in (0, 1): # caso base
       return 1
    return factorial(n - 1) * n # caso recursivo

"""
sys.getrecursionlimit()

Devuelve el valor actual del límite de recursión, la profundidad máxima de la pila del intérprete de Python. 
Este límite evita que la recursión infinita provoque un sobreflujo

"""
limit = sys.getrecursionlimit()
print("getrecursionlimit(): ", limit)
# getrecursionlimit():  1000

"""
sys.setrecursionlimit()

El límite máximo posible depende de la plataforma. 
Un usuario puede necesitar establecer el límite más alto cuando tiene un programa que requiere una recursión profunda y una plataforma que soporta un límite más alto. 
Esto debe hacerse con cuidado, ya que un límite demasiado alto puede llevar a un bloqueo.

Si el nuevo límite es demasiado bajo para la profundidad de recursión actual, se lanza una excepción RecursionError.

lanza una excepción RecursionError si el nuevo límite es demasiado bajo en la profundidad de recursión actual.

"""
print("sys.setrecursionlimit(): ", sys.setrecursionlimit(limit))
# sys.setrecursionlimit():  None

