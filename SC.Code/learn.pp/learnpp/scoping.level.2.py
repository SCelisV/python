#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
transcript: SCelis

# scoping.level.2.py

"""
def outer():
    test = 1 # outer scope
    print('outer - test: ', test)
    def inner():
        test = 2 # inner scope
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
global: 0
"""