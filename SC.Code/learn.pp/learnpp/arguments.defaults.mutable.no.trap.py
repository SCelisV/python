#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
transcript: SCelis

# arguments.defaults.mutable.no.trap.py

Los valores por defecto se crean en el momento de la def,
por lo tanto, las llamadas posteriores a la misma función posiblemente se comportarán de manera diferente según
la mutabilidad de sus valores por defect

es muy útil, por ejemplo, cuando se utilizan técnicas de memorización (ex: Google)

más interesante es lo que ocurre cuando, entre las llamadas, introducimos una que no utiliza valores por defecto,
los valores por defecto se conservan incluso si llamamos a la función con otros valores

¿cómo puedo obtener un nuevo valor vacío cada vez?

al utilizar esta técnica, si no se pasa a al llamar a la función, 
siempre se obtiene una lista nueva y vacía.

"""
# arguments.defaults.mutable.no.trap.py

def func(a=None):
    if a is None:
        a = []
        # ...
# haz lo que quieras con `a` ....
