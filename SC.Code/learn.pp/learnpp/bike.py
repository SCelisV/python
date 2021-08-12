#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 23:33:15 2021

@author: Fabrizio Romano
transcript: SCelis

# byke.py
# /home/hadoop/SCProjects/learn.pp/learnpp

clases
"""
class Bike:
    """# let's define the class Bike"""

    # es un inicializador.
    # configurar los objetos con los valores que le pasamos cuando lo creamos.
    # propiedades colour, frame_material
    def __init__(self, colour, frame_material):
        self.colour = colour
        self.frame_material = frame_material
    # método adicional para frenar la bici
    def brake(self):
        """ lets define the """
        print("Braking!")

# let's create a couple of instances
red_bike = Bike('Red', 'Carbon fiber')
blue_bike = Bike('Blue', 'Steel')

# let's inspect the objects we have, instances of the Bike class.
    # atributos del objeto colour, frame_meterial
    # conjunto de atributos de un objeto se considera un espacio de nombres
    # ex: red_bike.colour, blue_bike.colour
print(red_bike.colour) # prints: Red
print(red_bike.frame_material) # prints: Carbon fiber
print(blue_bike.colour) # prints: Blue
print(blue_bike.frame_material) # prints: Steel

# let's brake!- llamamos al metodo que va a frenar la bici red_bike.
red_bike.brake()                # prints: Braking!
