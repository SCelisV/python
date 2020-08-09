#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 19:01:32 2020
IN-WORK-OUT
@author: scelis
"""
#Esta es una forma de realizar una condición
#Vamos a inicializar la variable x en un número que digita el usuario por teclado, el programa imprimirá un mensaje dependiendo del valor que tenga esa variable.
x = 5
print('Antes ', x)
if (int(x) == 5): 
    print('Es 5')
    print('Sigue siendo 5')
    print('Third 5')
print ("Después 5")
print ("Antes 6")
if (int(x) == 6): 
    print('Es 6')
    print('Sigue siendo 6')
    print('Third 6')
print ("Después 6")

print('==========')
#se mantiene el incremento de la identación después de if or for
#decrementa la identación para indicar el fin del bloque

x = 5
if (x > 2):
    print('Mayor que 2')
    print('Sigue siendo mayor')
print('Final del bloque mayor que 2')

for i in range(5):
    print(i)
    if i > 2:
        print('Mayor que 2')
    print('Final del bloque for i es: ', i)
print('Todo hecho')

print('==========')

