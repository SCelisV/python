#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 12:45:18 2021

@author: Fabrizio Romano
transcript: SCelis

# switch.py

switch / case , that in Python is missing but
is perfectly capable of realizing such logic using if / elif / else statements.

# /home/hadoop/SCProjects/learn.pp/learnpp

looping programming
"""
# switch.py
DAY_NUMBER = 4
if 1 <= DAY_NUMBER <= 5:
    DAY = 'Weekday'
elif DAY_NUMBER == 6:
    DAY = 'Saturday'
elif DAY_NUMBER == 0:
    DAY = 'Sunday'
else:
    DAY = ''
    raise ValueError(str(DAY_NUMBER) + ' is not a valid day number.')
print(DAY)

"""

sentencias match

Una sentencia match toma una expresión y compara su valor con patrones sucesivos dados como uno o más bloques case. 
Es superficialmente similar a una sentencia switch en C, Java o JavaScript (....), 
pero también puede extraer componentes (elementos de la secuencia o atributos del objeto) del valor en variables.

"""

"""
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case 401 | 403 | 404:
            return "Not allowed"
        case _:                                                             # nunca deja de coincidir. Si ningún caso coincide, 
                                                                            # no se ejecuta ninguna de las ramas.
            return "Something's wrong with the internet"
"""

"""
Los patrones pueden parecerse a las asignaciones de desempaquetado, y pueden utilizarse para enlazar variables:
# point is an (x, y) tuple
"""
"""
match point:
    case (0, 0): # este patrón tiene dos literales, y puede considerarse como una extensión del patrón literal mostrado anteriormente. 
        print("Origin")
    case (0, y): # combinan un literal y una variable, 
                 # y la variable vincula un valor del sujeto (punto). 
        print(f"Y={y}")
    case (x, 0): # combinan un literal y una variable, 
                 # y la variable vincula un valor del sujeto (punto). 
        print(f"X={x}")
    case (x, y): # El cuarto patrón captura dos valores, 
                 # lo que lo hace conceptualmente similar a la asignación de desempaquetado (x, y) = punto.
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")

"""
"""
Los patrones pueden utilizar constantes con nombre. Estos deben ser nombres con puntos para evitar que sean interpretados como variables de captura:
"""
from enum import Enum
class Color(Enum):
    RED = 0
    GREEN = 1
    BLUE = 2

"""
match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :( ")

"""