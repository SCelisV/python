#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 21:48:39 2021

@author: Fabrizio Romano
transcript: SCelis

# dany.py
we want to tell whether at least one of the elements in a list evaluates to True
when we find it, we don't need to keep scanning the list any further.

establecer una variable de bandera, y luego iniciar la inspección.
Si encuentra un elemento que coincida con sus criterios,
entonces actualizas la bandera y dejas de iterar.
Después de la iteración, se inspecciona la bandera y toma la acción correspondiente

# /home/hadoop/SCProjects/learn.pp/learnpp

looping programming
"""
# any.py
items = [0, None, 0.0, True, 0, 7]      # True and 7 evaluate to True
FOUND = False                           # this is called "flag"
for item in items:
    print('scanning item', item)
    if item:
        FOUND = True                    # we update the flag
        break
if FOUND:                               # we inspect the flag
    print('At least one item evaluates to True')
else:
    print('All items evaluate to False')
