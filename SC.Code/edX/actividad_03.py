#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IN-WORK-OUT
Created on Fri Aug 21 21:33:37 2020

@author: scelis
actividad_03.py

"""
"""
1. Abre el conjunto de datos de la actividad de la semana anterior con ayuda de la librería Pandas utilizando un cuaderno nuevo de Python.

2. Genera los siguiente modelos utilizando la librería Scikit-learn:

            2.1 Modelo de regresión polinomial.

            2.2 Modelo de regresión basada en las máquinas de soporte vectorial.

            2.3 Modelo de regresión basada en el método de árboles de regresión.

3. Utiliza la instrucción df[“over5000”] = (df[“charges”] > 5000).map({False: 0, True: 1}) para agregar una variable que indique si el precio del servicio médico sobrepasa o no los $5000 dólares.

4. A partir de esos datos, generar un modelo de regresión logística y validarlo con una matriz de confusión.

5. Genera una imagen .png de tu matriz de confusión utilizando la instrucción dada o toma una captura de pantalla en formato .jpeg y cárgala en la plataforma de edX.

Instrucción a utilizar: 

import matplotlib.pyplot as plt

plt.savefig("figura.png")

6. Guarda todo el ejercicio hecho en tu libreta de Jupyter.

7. Guarda tus archivos en una carpeta comprimida y compartela en la plataforma de edX.

NOTA: PARA CARGAR DOS ARCHIVOS EN LA PLATAFORMA, DEBES INTEGRARLOS EN UN ARCHIVO COMPRIMIDO. EXISTEN SOFTWARES GRATUITOS COMO 7-ZIP QUE PERMITEN COMPRIMIR ARCHIVOS SATISFACTORIAMENTE..
"""