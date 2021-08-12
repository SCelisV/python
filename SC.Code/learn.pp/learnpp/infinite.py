#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 15:04:39 2021

@author: Fabrizio Romano
transcript: SCelis

# infinite.py
Infinite iterators
Infinite iterators allow you to work with a for loop , such as if it were a while loop:


# /home/hadoop/SCProjects/learn.pp/learnpp

looping programming
"""
#infinite.py
from itertools import count
for n in count(5, 3):                   # like range(5, 21, 3) = 5, 8, 11, 14, 17, 20
    if n > 20:
        break                           # We need to break it manually, 
                                        # otherwise it becomes an infinite loop.
    print(n, end=', ')                  # instead of newline, comma and space
    