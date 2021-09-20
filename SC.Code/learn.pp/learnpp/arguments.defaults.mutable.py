#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
transcript: SCelis

# arguments.defaults.mutable.py

Los valores por defecto se crean en el momento de la def,
por lo tanto, las llamadas posteriores a la misma función posiblemente se comportarán de manera diferente según
la mutabilidad de sus valores por defect

es muy útil, por ejemplo, cuando se utilizan técnicas de memorización (ex: Google)

"""
# arguments.defaults.mutable.py

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
func()
"""
[0]
{1: 1}
############
"""
func()
"""
[0, 1]
{1: 1, 2: 2}
############
"""