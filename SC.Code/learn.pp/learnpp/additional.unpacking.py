#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
transcript: SCelis

# additional.unpacking.py

desempaquetar múltiples iterables y diccionarios, y se unen correctamente bajo args y kwargs . 
esta característica es importante ya que nos permite no tener que fusionar args1 con args2 , y kwargs1 con kwargs2 en el código.

"""

# additional.unpacking.py

def additional(*args, **kwargs):            # desempaquetar múltiples iterables y diccionarios, y se unen correctamente bajo args y kwargs
    print(args)                             # (1, 2, 3, 4, 5)
    print(kwargs)                           # {'option1': 10, 'option2': 20, 'option3': 30}

args1 = (1, 2, 3)
args2 = [4, 5]
kwargs1 = dict(option1=10, option2=20)
kwargs2 = {'option3': 30}
additional(*args1, *args2, **kwargs1, **kwargs2)            #   es la forma de llamar a esta función. 

