#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
transcript: SCelis

# scoping.level.2a.py

"""
def outer():
    def inner():
        test = 2 # inner scope
        print('inner - test:', test)

    inner()
    print('outer - test:', test)

test = 0 # global scope
outer()
print('global:', test)

"""
inner - test: 2
outer - test: 0
global: 0
"""