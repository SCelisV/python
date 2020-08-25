#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IN-WORK-OUT
Created on Fri Aug 21 21:33:37 2020

@author: scelis
actividad_01.py

"""
"""
¿Es posible predecir la prima del seguro de pacientes según sus características? En esta actividad responderás esta pregunta. Las variables de estudio son:
Age: Edad del asegurado.
BMI: Índice de masa corporal del asegurado.
Children: Número de hijos que dependen del asegurado.
Charges: Variable a predecir. Cantidad asegurada en dólares.
Las instrucciones de la actividad son las siguientes:

    1. Descargar la base de datos insurance_clean.csv (Este archivo debe de colocarse en la misma carpeta que el cuaderno que utilices).

    2. Leer el conjunto de datos con la ayuda de la librería Pandas.

    3. Separar el conjunto de datos en dos variables ("X" para la columna "age" y "Y" para la variable de "charges")

    4. Separar las variables "X" y "Y" en conjuntos de entrenamiento y prueba, utilizando el método train_test_split de la librería sklearn.model_selection.

    5. Construir un modelo de regresión lineal usando "LinearRegresion" de la librería sklearn.linear_model, utilizando en el eje de las "x" solamente la columna correspondiente a la variable "age", y en el eje de las "y" la variable "charges".

    6. Evaluar el modelo con la métrica r2_score tanto en el conjunto de entrenamiento como en el de prueba.

    7. Repetir los pasos 5 y 6 sustituyendo la variable "age" por "BMI" y escribe en tu libreta de Jupyter por qué no es una variable relevante para realizar una predicción acertada del costo del servicio médico.

    8. Guardar todo el ejercicio hecho en tu libreta de Jupyter.

    9. Guarda el archivo en una carpeta comprimida.

    10. Comparte tu carpeta comprimida en la plataforma de edX.
"""