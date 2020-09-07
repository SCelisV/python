#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IN-WORK-OUT
Created on Fri Aug 21 21:33:37 2020

@author: scelis
actividad_02.py

"""
"""
1. Abrir el conjunto de datos “Mall_Customers.csv” con ayuda de la librería Pandas utilizando un cuaderno nuevo de Python.

2. Analiza el conjunto de datos con la función “head” y los atributos “shape” y “dtypes” para que puedas responder las siguientes preguntas, incluye tus respuestas en la misma libreta en una celda del tipo “markdown”:

a)     ¿Cuáles son los nombres que reciben las columnas en el conjunto de datos?

b)     ¿Cuáles son los tipos de datos asociados a las columnas?

c)      ¿Cuál es la cantidad total de registros que tiene este conjunto de datos?

3. Una vez identificada la columna “Gender”, es necesario que cambies el tipo de dato de esta columna al tipo “int” utilizando la instrucción vista en la libreta de la tercer semana titulada “Mejorando los modelos”.

4. Asigna la columna “CustomerID” como el índice de los datos.

5. Realiza una transformación de los datos a valores flotantes.

6. Utilizando las columnas “Spending Score” y “Annual Income”, realiza un agrupamiento de datos con el algoritmo “K-Means” con K = 3. Nota: En caso de ser necesario, guíate siguiendo el ejemplo encontrado en la libreta “Clustering y K-Means”.

7. Utilizando el método del codo (elbow), determina el número óptimo de Clusters y repite el paso 6 modificando el número de Clusters (parámetro K) por el valor obtenido.

8. Realiza la gráfica de dispersión con los clusters definidos.

9. Analiza la gráfica de dispersión obtenida, identifica y describe el perfil de cliente por cluster. Incluye tus respuestas en la misma libreta en una celda del tipo “markdown”.

10. Guardar todo el ejercicio hecho en tu libreta de Jupyter, adjuntalo en un archivo. zip y comparte el archivo en la plataforma de edX.
"""