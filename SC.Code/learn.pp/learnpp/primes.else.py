#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 01:02:52 2021

@author: Fabrizio Romano
transcript: SCelis

# primes.else.py

A prime number (or a prime) is a natural number greater than 1 that has no positive
divisors other than 1 and itself. A natural number greater than 1 that is not a prime
number is called a composite number.

If we consider the first 10 natural numbers,
we can see that 2, 3, 5, and 7 are primes,
while 1, 4, 6, 8, 9, and 10 are not.
In order to have a computer tell you whether a number, N, is prime,
you can divide that number by all natural numbers in the range [2, N).
If any of those divisions yields zero as a remainder, then the number is not a prime.

range(2,hasta) ==> [2, hasta),
Por lo tanto
range(2, upto + 1) ==> [2, upto + 1) ==> [2, hasta]

# /home/hadoop/SCProjects/learn.pp/learnpp

looping programming
"""
# primes.else.py
primes = []
UPTO = 100
for n in range(2, UPTO + 1):
    for divisor in range(2, n):
        if n % divisor == 0:
            break
    else:
        primes.append(n)
print(primes)
