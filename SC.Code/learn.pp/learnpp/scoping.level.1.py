#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
transcript: SCelis

# scoping.level.1.py

Pythonic form

"""
test = 2 # this is defined in the global scope
print('global - test: ', test)

def my_function():
    test = 1            # this is defined in the local scope of the function
    print('en la llamada a my_function - test:', test)

test = 0 # this is defined in the global scope

print('antes de llamar a la función: global: - test: ', test)

my_function()

print('después de llamar a la función global: - test: ', test)
