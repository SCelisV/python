#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 19:01:32 2020
IN-WORK-OUT
@author: scelis
"""
#Esta es una forma de realizar una condición
#Vamos a inicializar la variable x en un número que digita el usuario por teclado, el programa imprimirá un mensaje dependiendo del valor que tenga esa variable.
x = input("Digite un número: ")

if (int(x) == 5): 
    print (x, " => Equals 5")
if (int(x) > 4):
    print(x, " => Greater than 4")
if (int(x) >= 5):
    print(x, " => Greater than or Equals 4")
if (int(x) < 6): print(x, " => Less than 6")
if (int(x) <= 5):
    print(x, " => Less than or Equals 5")
if (int(x) != 6):
    print(x, " => Not equal 6")