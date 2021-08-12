#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 23:33:15 2021

@author: Fabrizio Romano
transcript: SCelis

# scopes1.py
# /home/hadoop/SCProjects/learn.pp/learnpp

Scopes - Alcances - local, enclosing, global, built-in (LEGB).
https://docs.python.org/3/tutorial/classes.html
"""
# Local versus Global

def local():
    """define a function called local"""
    # ambito local
    variable = 7
    print(variable)

    # ambito global
    variable = 5
    print(variable)

# we call, or `execute` the function local
local()

# python scopes1.py
# variable defined both
# - in the global scope and
# - in the local one (the one defined by the local function).
 