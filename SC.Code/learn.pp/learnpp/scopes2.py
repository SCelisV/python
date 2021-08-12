#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 23:33:15 2021

@author: Fabrizio Romano
transcript: SCelis

# scopes2.py
# /home/hadoop/SCProjects/learn.pp/learnpp

Scopes - Alcances - local, enclosing, global, built-in (LEGB).
https://docs.python.org/3/tutorial/classes.html
"""

def local():
    """define a function called local"""
    # variable doesn't belong to the scope defined by the local function
    # so Python will keep looking into the next enclosing scope.
    # variable is finally found in the global scope
    # VARIABLE = 7
    print(VARIABLE, 'printing from the local scope')
VARIABLE = 5
print(VARIABLE, 'printing from the global scope')

# we call, or `execute` the function local
local()
