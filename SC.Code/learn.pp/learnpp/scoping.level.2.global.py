#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
transcript: SCelis

# scoping.level.2.global.py

"""
def outer():
    test = 1 # outer scope
    print('outer - test: ', test)
    def inner():
        global test                             # hace que la variable global tome el valor assignado aquí
        test = 2 # global scope              
        print('inner - test:', test)

    inner()
    print('outer - test:', test)            

test = 0 # global scope
outer()
print('global:', test)

"""
outer - test:  1
inner - test: 2
outer - test: 1
global: 2
"""