#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
transcript: SCelis

# arguments.defaults.mutable.intermediate.call.py

Los valores por defecto se crean en el momento de la def,
por lo tanto, las llamadas posteriores a la misma función posiblemente se comportarán de manera diferente según
la mutabilidad de sus valores por defect

es muy útil, por ejemplo, cuando se utilizan técnicas de memorización (ex: Google)

más interesante es lo que ocurre cuando, entre las llamadas, introducimos una que no utiliza valores por defecto,
los valores por defecto se conservan incluso si llamamos a la función con otros valores

"""
# arguments.defaults.mutable.intermediate.call.py

def func(a=[], b={}):       # tienen valores por defecto mutables. por lo tanto, si afecta a esos objetos, 
                            # cualquier modificación se mantendrá en las siguientes llamadas a la función
    print(a)
    print(b)
    print('#' * 12)
    print('\n')
    a.append(len(a))            # esto afectará al valor por defecto de a
    b[len(a)] = len(a)          # esto afectará al valor por defecto de b

func()
"""
[]
{}
############
"""
func(a=[1, 2, 3], b={'B': 1})   # que ocurre cuando, entre las llamadas, introducimos una que no utiliza valores por defecto,
"""
[1, 2, 3]
{'B': 1}
############
"""
func()                          #  los valores por defecto se conservan incluso si llamamos a la función con otros valores
"""
[0, 1]
{1: 1, 2: 2}
############
"""