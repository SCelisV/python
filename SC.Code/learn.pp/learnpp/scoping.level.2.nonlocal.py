#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
transcript: SCelis

# scoping.level.2.nonlocal.py

"""
def outer():
    test = 1 # outer scope
    print('outer - test: ', test)
    def inner():
        nonlocal test
        test = 2 # inner scope              nearest enclosing scope (which is 'outer')
        print('inner - test:', test)

    inner()
    print('outer - test:', test)            # nonlocal en inner hace que el alcance aumenta al más cercano en este caso outer

test = 0 # global scope
outer()
print('global:', test)

"""
outer - test:  1
inner - test: 2
outer - test: 2
global: 0
"""