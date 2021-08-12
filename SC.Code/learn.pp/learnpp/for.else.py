#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 22:09:41 2021

Created on Wed Aug 11 21:48:39 2021
Created on Wed Aug 11 23:03:49 2021

@author: Fabrizio Romano
transcript: SCelis

# for.else.py
we want to tell whether at least one of the elements in a list evaluates to True
when we find it, we don't need to keep scanning the list any further.

un bucle for que itera sobre un grupo de elementos,
buscando uno que coincida con alguna condición.
En caso de que no encontramos al menos uno que satisfaga la condición,
queremos lanzar una excepción.

Esto significa que queremos detener la ejecución regular del programa y señalar que hubo un
error, o excepción, que no podemos resolver.

si no se encuentra un driver, se lanza una DriverException, indicando al
programa que la ejecución no puede continuar

La excepción se lanza como parte de la lógica del bucle for
porque el bucle for está comprobando alguna condición

# /home/hadoop/SCProjects/learn.pp/learnpp

looping programming
"""

# for.else.py
class DriverException(Exception):
    """ This class busca DRIVER, si no lo encuentra lanza una exception """
    #pass

people = [('James', 17), ('Kirk', 9), ('Lars', 13), ('Robert', 8)]
for person, age in people:
    if age >= 18:
        DRIVER = (person, age)
        break
else:
    raise DriverException('Driver not found.')
    