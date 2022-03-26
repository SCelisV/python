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
from xml.dom.expatbuilder import Namespaces


class Bike:
    """# let's define the class Bike"""

    # __double underscores__ method is a magic method
    # es un metodo inicializador.
    # configurar los objetos con los valores que le pasamos cuando lo creamos.
    # propiedades colour, frame_material
    def __init__(self, colour, frame_material):
        self.colour = colour
        self.frame_material = frame_material

    # método adicional para frenar la bici - it contains just a print statement,
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

# para llegar a la propiedad frame_material a través de diferentes Namespaces( red_bike , blue_bike ), 
# obtenemos valores diferentes. No hay solapamiento ni confusión.

# El operador punto ( . ) es, por supuesto, el medio que utilizamos para entrar en un namespaces, en el caso de los objetos.

print(red_bike.colour) # prints: Red
print(red_bike.frame_material) # prints: Carbon fiber
print(blue_bike.colour) # prints: Blue
print(blue_bike.frame_material) # prints: Steel

# let's brake!- llamamos al metodo que va a frenar la bici red_bike.
red_bike.brake()                # prints: Braking!
