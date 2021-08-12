#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 19:02:20 2021

@author: Fabrizio Romano
transcript: SCelis

# binary.py
The while loop: doesn't loop over a sequence
use when you just need to loop until some condition is satisfied,
or even loop indefinitely until the application is stopped,
or maybe where we don't really have something to iterate o
We want to print the binary representation of a positive number.
we can use a simple algorithm that collects the remainders of division by 2 (in reverse order),
and that turns out to be the binary representation of the number itself:
6 / 2 = 3 (remainder: 0)
3 / 2 = 1 (remainder: 1)
1 / 2 = 0 (remainder: 1)
List of remaindeers 0, 1, 1.
Inverse is 1, 1, 0, which is also the binary representation of 6: 110

calculate the binary representation for the number 39: 100111

# /home/hadoop/SCProjects/learn.pp/learnpp

looping programming
"""
# binary.py
N = 39
remainders = []
while N > 0:
    #print(N)
    REMAINDER = N % 2                   # remainder of division by 2
    #print(REMAINDER)
    remainders.insert(0, REMAINDER)     # we keep track of remainders
    #print(remainders)
    N //= 2                             # we divide N by 2
    #print(N)
print(remainders)
    