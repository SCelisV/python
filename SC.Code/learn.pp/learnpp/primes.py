#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 00:07:28 2021

@author: Fabrizio Romano
transcript: SCelis

# primes.py

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

# primes.py
primes = []                             # this will contain the primes in the end
UPTO = 100                              # the limit, inclusive
for n in range(2, UPTO + 1):
    IS_PRIME = True                     # flag, new at each iteration of outer for
    for divisor in range(2, n):         # cuando n es 2, el bucle más interno
                                        # ni siquiera se ejecuta,
                                        # range(2, 2) ==> [2, 2), 2 esta excluido
        if n % divisor == 0:
            IS_PRIME = False
            break
    if IS_PRIME:                    # check on flag
        primes.append(n)
print(primes)
