#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
transcript: SCelis

# return.single.value.2.py 

https://docs.python.org/3.8/library/functools.html?highlight=reduce#functools.reduce

def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value

https://docs.python.org/3.8/library/operator.html?highlight=mul#operator.mul

operator.mul(a, b)
operator.__mul__(a, b)

    Return a * b, for a and b numbers.

Pythonic form 

"""
# return.single.value.2.py

from functools import reduce
from operator import mul

def factorial(n):
    return reduce(mul, range(1, n + 1), 1)          # reduce(function, iterable, initializer=None):

f5 = factorial(5)
print(f5)                       #   120