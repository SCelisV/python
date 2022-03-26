#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Fabrizio Romano
transcript: SCelis

# functions.defining.py
Fibonacci series up to n
We want to print a pair person/age on one line for all of the both list
Pythonic form

# /home/hadoop/SCProjects/0_SCProjects_github.com_SCelisV/python/SC.Code/learn.pp/learnpp/functions.defining.py

"""
def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Now call the function we just defined:
fib(2000)       # 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597
