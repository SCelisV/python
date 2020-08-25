#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IN-WORK-OUT
Created on Thu Aug 20 00:28:58 2020

@author: scelis
matplotlib.pyplot es un conjunto de funciones que hacen que matplotlib funcione como MATLAB. 
Cada función pyplot realiza algún cambio en una figura: por ejemplo, 
crea una figura, crea un área de trazado en una figura, 
traza algunas líneas en un área de trazado, 
decora el trazado con etiquetas, etc.
matplot_library.py
https://matplotlib.org
"""

# Le decimos a python que grafique en el mismo fichero
# Mute inline plotting

import matplotlib.pyplot as plt

# Creamos un scatter plot con los datos de entrenamiento
plt.scatter(X_train, y_train, color="blue")

# Creamos un scatter plot con los datos de prueba
plt.scatter(X_test, y_test, color="orange")

# Graficamos el modelo
plt.plot(X_plot, y_plot,"r--")



