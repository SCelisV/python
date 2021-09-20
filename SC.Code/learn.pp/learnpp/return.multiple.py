#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
transcript: SCelis

# return.multiple.py

Devolver múltiples valores es muy fácil, sólo tienes que usar tuples (de forma explícita o implícita). 

imita la función incorporada divmod

# return (a // b, a % b)        # devuelve tanto el resultado (a // b) de la división
                                # y el resto de la división (a % b), al mismo tiempo. - tupla explicita

"""

# return.multiple.py

def moddiv(a, b):
    return a // b, a % b        # devuelve tanto el resultado y el resto de la división, al mismo tiempo. - tupla implicita

print(moddiv(20, 7))            # imprime (2, 6)