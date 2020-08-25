#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IN-WORK-OUT
Created on Fri Aug 21 19:33:55 2020

@author: SCELIS
# numpy_library.py - for arrays and operations with arrays
https://numpy.org
"""

import numpy as np

# devuelven muestras numéricamente espaciadas, calculadas sobre el intervalo
X_plot = np.linspace(0,40) # ordenados por fila 
print(X_plot)
X_plot = np.linspace(0,40).reshape(-1, 1) # ordenados por columna
print(X_plot)

