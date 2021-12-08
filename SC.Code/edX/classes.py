"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
*********************
* Created on Sat Aug  7 22:24:26 2021
*********************
* classes.py
*********************
* Version: 001
*********************
* @authors: SCelis
*********************
* Copyright (c) 2021 SCelis
* All Rights Reserved.
*********************
* Pruebas con classes
*********************
* ChangeLog:
*
*   iSCelis@rev 001: Create
*
**********
* TODO: ??
**********
* Description: Pruebas con fechas
****
*
"""
class Car:
    speed = 0
    started = False
 
    def start(self):
        self.started = True
        print("Car started, let's ride!")
 
    def increase_speed(self, delta):
        if self.started:
            self.speed = self.speed + delta
            print('Vrooooom!')
        else:
            print("You need to start the car first")
 
    def stop(self):
        self.speed = 0
        print('Halting')

# creating minimal classes:
class MyEmptyClass:
    pass


# Otro lugar donde se puede utilizar el pass es como marcador de posición para una función o cuerpo condicional cuando se está trabajando en un nuevo código, lo que le permite seguir pensando en un nivel más abstracto. El pass se ignora silenciosamente:

def initlog(*args):
    pass   # Remember to implement this!


"""
puedes usar el nombre de la clase seguido de una lista de argumentos parecida a un constructor, 
pero con la capacidad de capturar atributos en variables:
"""

class Point:
    x: int
    y: int


def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")

