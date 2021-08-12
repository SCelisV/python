#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 23:33:15 2021

@author: Fabrizio Romano
transcript: SCelis

# scopes3.py
# /home/hadoop/SCProjects/learn.pp/learnpp

Scopes - Alcances - local, enclosing, global, built-in (LEGB).
the enclosing scope:
https://docs.python.org/3/tutorial/classes.html
"""

def enclosing_func():
    """Local, Enclosing and Global"""
    variable = 13

    def local():
        # m doesn't belong to the scope defined by the local
        # function so Python will keep looking into the next
        # enclosing scope. This time m is found in the enclosing
        # scope
        print(variable, 'printing from the local scope')
    # calling the function local
    local()
variable = 5
print(variable, 'printing from the global scope')
enclosing_func()
