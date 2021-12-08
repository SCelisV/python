"""
@author: Fabrizio Romano
transcript: SCelis

# primes.py

función para generar una lista de números primos hasta un límite. 

no es necesario dividirlo entre todos los números de 2 a N-1 para decidir si un número, N, es primo. 
es suficiente calcular hasta √N. 

no es necesario probar la división para todos los números de 2 a √N, sólo los primos en ese rango. 

sólo se prueba la divisibilidad usando los primos previamente calculados y nos detenemos una vez que el divisor de prueba es mayor que la raíz del candidato. 

Usamos la lista de resultados de la lista de primos para obtener los primos de la división. 

# /home/hadoop/SCProjects/learn.pp/learnpp

"""

from math import sqrt, ceil

def get_primes(n):

    """Calculate a list of primes up to n (included). """

    primelist = []

    for candidate in range(2, n + 1):
        is_prime = True
        """el valor de la raíz = el valor entero del techo de la raíz del candidato a primo""" 
        """ó podria ser = int(k ** 0,5) + 1 """
        root = ceil(sqrt(candidate)) # division limit
        for prime in primelist: # probar solamente los primos de la división
            if prime > root: # no necesitas chek nada más
                break
            if candidate % prime == 0:
                is_prime = False
                break
        if is_prime:
           primelist.append(candidate)
    return primelist


print("get_primes(100): ", get_primes(100))
"""
get_primes(100):  [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
"""