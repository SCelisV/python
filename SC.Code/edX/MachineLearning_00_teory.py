# MachineLearning_00_teory.py
# MachineLearning_00_code.py
""" 
# Código del cálculos de los módelos:
    - regresión ĺineal, 
    - regresión múltiple, 
    - regresión polinomial, 
    - Máquinas de Soporte Vectorial - Support Vector Regression
    - Árboles de decisión
    
# BostonDataSet
# =============================================================================
""" 

# Módelos predictivos con Machine Learning - MPML - SCProjects/0_SCProjects_github.com_SCelisV/python/SC.Code/jupyter/MPML
""" Analizar datos - O-J-O-

    Revisar la descripción de los datos, utilizando el método describe() like summary on RStudio.
    Utilizar la media y la mediana para determinar la tendencia central.
    Tener especial atención a los percentiles para poder identificar los rangos de los datos.
    Usar una matriz de correlación para identificar las relaciones fuertes en los datos.
    Hacer visualizaciones para mejorar tu entendimiento de los datos (Box plot, Density plot, Scatter plot).
    Limpiar tus datos (NA, outliers). """

# https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html - include in anaconda3


"""     

    Predecir una clase, tenemos un problema de clasificación.
Applications: Spam detection, image recognition.
Algorithms: SVM, nearest neighbors, random forest, 

    Predecir un valor numérico, tenemos un problema de regresión.
Applications: Drug response, Stock prices.
Algorithms: SVR, nearest neighbors, random forest, 

    Separar los datos en diferentes grupos, tenemos un problema de agrupamiento.
Applications: Customer segmentation, Grouping experiment outcomes
Algorithms: k-Means, spectral clustering, mean-shift,

    Si queremos simplificar la información, tenemos un problema de reducción de dimensiones (reducir la dimensión del problema)
 
"""

# Machine learning => automatiza la construcción de un módelo analítico, uso de algoritmos que aprende de los datos.

# Algoritmos => Supervisado, NO Supervisado, De Refuerzo

# =============================================================================
"""
# 1. -> Regresión líneal - Supervisado - Aproximación que modela una relación entre una variable escalar dependiente ("Y") y una o más variables explicativas/independientes ("X")
"""
# Dibujará una recta y=mx+b => que nos indicará la tendencia del conjunto de datos, y nos ayudará a predecir en función de un valor X un valor Y. 
# Ecuación matemática que representa una línea recta. 
# Intentará pasar por la mayor cantidad de datos posibles.
# Es la representación mas adecuada de la distribución de los datos en un diagrama de dispersión
# y => coordenada Y
# m => pendiente
# x => coordenada X
# b => Ordenada en el Origen, intercepción, el punto Y donde la línea cruza el eje Y, relación X,Y

# Procedimiento manual:
# El procedimiento para generar la regresión líneal utilizando la técnica de ajuste de mínimos cuadrados:
    
# - calcular la media aritmética y la varianza tanto de los valores de _x_ como los valores de _y_. 

# Por lo que construiremos una tabla donde calculamos los valores cuadrados de ambas variables y calculamos la sumatoria de cada columna.
# formulas: img/RegLin_Formulas.png

# sumatoria x =>
# sumatoria y =>
# sumatoria x*y => 
# sumatoria x² =>
# sumatoria y² =>
#
# y=-0.8926x+31.9160 cambiando el valor de x y pintandola en el plano obtenemos la recta de puntos.

# al unir las graficas de la recta de puntos y los datos originales, 
# se puede observar que tienen comportamientos similares
# por lo tanto por medio de la ecuación podemos predecir el comportamiento de otros datos.

"""
# 2. -> Regresión Múltiple - Supervisado - Utilizamos regresión múltiple cuando estudiamos la posible relación entre varias variables independientes (predictoras o explicativas) y otra variable dependiente (criterio, explicada, respuesta). ... Las modelos de regresión nos informan de la presencia de relaciones, pero no del mecanismo causal.
"""
# Multiples variables independientes en el mismo módelo.
# Importante saber elegir las variables independientes
# =============================================================================
"""
# 3. -> Regresión polinomial - Supervisado - 
"""
# Es parecida a la regresión líneal sólo que extiende la función a un polinomio flexible que se puede curvar si es necesario.. etc. 
# Representa una curva, y graficará el polinomio que más se parezca a las características de los datos.
# Este modelo añade curvatura al elevar la variable _x_ a diferentes potencias. De esta manera, se pueden conseguir diferentes funciones que representan y se ajustan más a la distribución de los datos.
# El procedimiento para generar la regresión cuadrática utilizando la técnica de ajuste de mínimos cuadrados inicia construyendo un sistema de ecuaciones que son producto de analizar la suma de los cuadrados de los residuos 
# Parabola = Polinomio de grado 2 = X² = potencia más grande - Derivadas parciales - 
# 
# =============================================================================
"""
# 4. -> Máquinas de Soporte Vectorial -> SVM -> SVR - Supervisado
"""
# Buscan encontrar un hiperplano que separe los puntos compuestos en una categoria de otra. 
# Delimitar con notoriedad cada una de las características de los diferentes conjuntos.
# Las máquinas de soporte vectorial buscan encontrar un hiperplano que separe de forma óptima a los puntos que componen diferentes categorías unos de los otros. 
# Este tipo de algoritmo suele utilizarse para predecir a que categoría pertencerá un nuevo punto del que no se tenía información con anterioridad.
# SVR -> Regresión de Soporte Vectorial - Supervisado - SVR
# Support Vector Regression es un algoritmo de regresión basado en las máquinas de soporte vectorial utilizados para clasificar elementos de diferentes conjuntos. 
# En la siguiente sección se explicara cómo funciona el algoritmo SVR con datos lineales, 
# pero es importante saber que este algoritmo también funciona para datos no lineales.

# Objetivos: Máximizar el margen(las bandas de soporte que rodean a la línea de regresión) para abarcar la mayoría de los puntos de nuestro módelo y Minimizar el error

#     https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR
#     https://scikit-learn.org/stable/modules/svm.html#tips-on-practical-use
# 
# =============================================================================
"""
# 5. -> Árboles de decisión : NO Supervisado
"""
# https://web.fdi.ucm.es/posgrado/conferencias/JorgeMartin-slides.pdf
# CART - Árboles de clasificación (asigna una etiqueta) y regresión (asigna una valor) 
# pretenden explicar o predecir una variable a partir de un conjunto de variables predictoras utilizando un conjunto de reglas sencillas. 
# Se hacen diferentes intervalos y a cada uno se asigna un valor de tal forma se podrá identificar cada punto a que rango pertenece
# El procedimiento para generar un árbol de regresión empieza partiendo la totalidad del intervalo de los datos de la variable independiente x en diferentes intervalos pequeños. En nuestro ejemplo aprovecharemos que es posible identificar que los datos parecen estar agrupados en los siguientes cuatro intervalos:
    
# =============================================================================
#     𝐼𝑛𝑡𝑒𝑟𝑣𝑎𝑙𝑜1: 0 ≤ 𝑥 < 0.25 => 𝑦=10
#     𝐼𝑛𝑡𝑒𝑟𝑣𝑎𝑙𝑜2: 0.25 ≤ 𝑥 < 0.5 => 𝑦=15
#     𝐼𝑛𝑡𝑒𝑟𝑣𝑎𝑙𝑜3: 0.5 ≤ 𝑥 < 0.75 => 𝑦=20
#     𝐼𝑛𝑡𝑒𝑟𝑣𝑎𝑙𝑜4: 0.75 ≤ 𝑥 ≤ 1.0 => 𝑦=15
#    
#    Asignarle un valor numérico a una entrada x de la cuál no se conocía su valor de salida y previamente.
# =============================================================================


"""
# 6. -> Redes neuronales => recibir, procesar y transmitir información
"""
# Perceptrón => neurona artificial, la unión de varios crean una red neuronal artificial. <=> simulan a las humanas y son capaces de transmitir señales entre ellas e ir modificando las entradas de las neuronas para obtener valores de salida
# Aprenden a partir de la experiencia para predecir

# Se compone de:
# - Canales/Señales de entrada - Dentritas
# - Función de activación - Soma o núcleo - (unión sumadora)
# - Canal de salida y Axón.

"""  n
 Σ WiXi + b
i=0  """


# Tipos de aprendizaje => Algoritmos => Supervisado, NO Supervisado, De Refuerzo

""" Aprendizaje supervisado => proporcionamos datos de test(conocidos)
Los algoritmos de aprendizaje supervisado son aquellos que trabajan primeramente aprendiendo con un conjunto de datos de entrenamiento "etiquetados", los cuales recibe para posteriormente trabajar con ellos, intentando asignarles correctamente una etiqueta que coincida con la que previamente tenía. """

""" El comportamiento del algoritmo se corrige en medida a cuántas veces fallo al momento de etiquetar los datos de prueba y posteriormente modifica su comportamiento para las próximas ejecuciones. Después de terminar de entrenar con los datos etiquetados, se somete al algoritmo a trabajar con un conjunto de datos nuevos para los que no se conoce la etiqueta. 
 """
# Supervisado => necesita datos previamente etiquetados(lo que es correcto y lo que no es correcto) para aprender a realizar el trabajo. En base a esto, el algoritmo aprenderá a resolver problemas futuros similares.a

# -> Regresión líneal,
# -> Regresión polinomial,
# -> Máquinas de Soporte Vectorial -> SVM - SVR

""" Aprendizaje no supervisado

Los algoritmos de aprendizaje no supervisado no cuentan con un conjunto de datos "etiquetados" con los cuales puede entrenar y buscan intentar encontrar algún tipo de organización o patrón en los datos de entrada que recibe. Estos algoritmos suelen tener un comportamiento "exploratorio", y en el caso de enfrentar un problema de agrupamiento, estos algoritmos intentan agrupar a los datos por medio de características similares pero no sin saber previamente que tipos de datos va a agrupar. 
 """
 
# NO Supervisado => necesita indicaciones previas, No necesita datos previamente etiquetados. Aprende a comprender y a analizar la información. Práctica sobre los datos que tiene. 
# Busca relaciones entre los datos - para identificarlos - pero no los podrá "etiquetar"

# -> K vecinos más cercanos - KNN
# -> Árboles de decisión :  https://web.fdi.ucm.es/posgrado/conferencias/JorgeMartin-slides.pdf
#   CART - Árboles de clasificación y regresión 
# pretenden explicar o predecir una variable a partir de un conjunto de variables predictoras utilizando un conjunto de reglas sencillas. 
# -> Random Forest -> Bosques Aleatorios
# -> k-medias -> no supervisado, usado para clusterización

""" 

Aprendizaje reforzado

Las técnicas de aprendizaje por refuerzo se basan en modificar la respuesta del algoritmo utilizando un proceso de retroalimentación basado en un conjunto de recompensas y castigos que le permiten al algoritmo identificar cuando alguna de las acciones que realizo previamente obtuvo buenos resultados o fue un comportamiento que deberá evitar en futuras ejecuciones. Estas técnicas de aprendizaje intentan simular el proceso de aprendizaje humano, simulando la sensación de que el algoritmo aprende obteniendo información de cómo se modifica el mundo que lo rodea en respuesta de las acciones que produce.  """

# De Refuerzo => aprende por su cuenta, en base a conocimientos introducidos previamente, aprende en función del éxito ó fracaso.
# La acción le puede generar una recompensa y la repites.. si es un castigo lo evitas 


# scikit-learn.org/ -- Machine Learning en Python 
# https://scikit-learn.org/stable
""" 
https://scikit-learn.org/stable/modules/classes.html#module-sklearn.datasets

https://scikit-learn.org/stable/datasets/index.html#boston-dataset
 """





# limpieza de datos
# verificar los null's


# si NULOS => FALSE => NO hay null's

# calculamos el coeficiente de CORrelación
# NO Diagonales => Correlación —> entran escalados entre -1 y 1.
# Si las variables están muy correlacionadas R tendrá valor entre -1 y 1.
# Existen dos tipos de correlaciones tanto negativas como positivas
# Correlación positiva => > 0 , aumenta una variable por tanto aumenta la otra.
# ex: Estatura - Peso - crecen a la vez.
# Correlación negativa => < 0, aumenta una variable y disminuye la otra.
# ex: Velocidad vs Autonomía. > aceleración < autonomía

# Cuando están más cercanos a 1, la nube de puntos va a ser más perfecta a una línea.
# si hay alguna correlación que me dé 1.00000000 podemos decir que es una
# correlación perfecta., ó que esas dos variables son la misma variable, independiente de las
# unidades en que este medida.
# correlación baja está entre -0,2 y +0,2
# Valores altos => cercano a -1 ó +1 —> en la primera fila y primera columna.
# Valores bajos => cercanos a 0 => resto de elementos entre la segunda fila y la diagonal.
# R: = 0 => Indica que no tienen nada de correlación.
# R: = 1 => Correlación Perfecta.

# R makes it easy to combine multiple plots into one overall graph, using either the
# par( ) or layout( ) function.

# With the par( ) function, you can include the option mfrow=c(nrows, ncols) to create a matrix of nrows x ncols plots that are filled in by row. mfcol=c(nrows, ncols) fills in the matrix by columns.


# - Cual es la probabilidad de un evento mas desfavorable.
# p-value -> indica si el regresor influye ó no influye en la variable de respuesta.
# p-value: < 2.2e-16 si < 0.05 => indica si el regresor influye , es decir, influye con un 95%.
# Si p-value: < 0.05 Influye
# Si p-value > 0.05 No tenemos evidencia para decir que influye significativamente.


# Una recta de regresión debe cumplir:
# Que la distancia entre los puntos a la recta de regresión sea mínima.

# Hipótesis de Partida - Diagnosis
# - Linealidad -> Se DA por supuesta - Las variables siguen una relación lineal.
# - Normalidad -> Se debe comprobar que los residuos siguen una distribución normal
#     La Y para TODAS las X NO sigue una distribución normal.. PERO
#     La variable Y para un determinado valor de X SI sigue una distribución normal.
# - Homocedasticidad -> varianza constante ó variabilidad constante - distribución de probabilidad de idéntica amplitud para cada variable aleatoria -
    # La nube de puntos tenga un grosor constante.
    # Heterocedastico -> varianza NO es constante ó variabilidad NO constante, a pesar de que la nube de puntos tiene forma lineal la varianza ó dispersión va aumentando:
# - Independencia -> Cuando las observaciones en sí no están relacionadas.



# R-squared: # Somos capaces de explicar el 77% de la variación de G3.

# 2. -> Regresión logística - Supervisado - Predecir el resultado de una variable categorica en función de otras independientes.
# Modela la probabilidad de que un evento ocurra en función de otros factores, método de clasificación (binaria, 1 ó 0).
# Dibujará una curva que nos indicará la tendencia del conjunto de datos, y nos ayudará a predecir en función de un valor X un valor Y.
# Siempre será entre 0 ó 1

# Si resultado >= 0.5 => devuelve 1
# Si resultado < 0.5 => devuelve 0


# Matriz de Confusión => Compara el valor real con el valor de prediccion

# Real vs predicción

# SI vs SI => PC => Positivo Correcto
# NO vs NO => NC => Negativo Correcto
# SI vs NO => FP => Falsos Positivos => Error Tipo 1
# NO vs SI => FN => Falsos Negativos => Error Tipo 2

# La precisión sirve para saber la probabilidad de acierto en la predicción => (PC + NC ) / Total
# La tasa de error sirve para saber la probabilidad de error en la predicción => (FP + FN) / Total

# API Command => kaggle kernels pull alexisbcook/titanic-tutorial

# Para limpiar estos datos lo que haremos será sustituir los valores NA de las edades por la media de edad en cada Pclass

# One Way
# creamos una función que reemplace los valores nulls del dataSet por 0, le pasamos la columna edad, y la columna clase
# =============================================================================
# nulos <- function(Age, Pclass) {
#     newAge <- Age
#     for(i in 1:length(Age)){
#         if( is.na(Age[i]) ) { # si es null
#             if(Pclass[i] == 1){
#                 newAge[i] <- 33.00
#             } else if(Pclass[i] == 2){
#                 newAge[i] <- 28.00
#             } else if(Pclass[i] == 3){
#                 newAge[i] <- 18.00
#             }   
#         }        
#     }
#     return(newAge)
# }
# =============================================================================

# =============================================================================
# # Funciones con varios argumentos y aplicar el resultado a una columna
# datos.19$Age <- nulos(datos.19$Age, datos.19$Pclass)
# 
# 
# # Two Way
# # creamos una función que reemplace los valores nulls del dataSet por 0, para poder calcular la media
# 
# factor(datos.19$Pclass)
# 
# nulos <- function(x) {
#     #print(x)
#     if( is.na(x) )
#         {return (0)}
#     else
#         {return (x)}
# }
# 
# =============================================================================


# Three Way - Otra forma de codificar la función..
# creamos una función que reciba la edad y la clase, reemplaza los valores nulls del dataSet por la media que corresponda con la clase:
# =============================================================================
# nulos <- function(x, y) {
#     # x => edad => datos.19$Age
#     # y => class => datos.19$Pclass
#     print(x)
#     print(y)
#     if (y == 1){
#         if( is.na(x) )
#             {return (33)}
#         else
#             {return (x)}
#     } else if (y == 2) {
#             if( is.na(x) )
#                 {return (28)}
#             else
#                 {return (x)}
#     } else if (y == 3) {
#             if( is.na(x) )
#                 {return (18)}
#             else
#                 {return (x)}
#     }
#     else {return (x)}
# }
# 
# =============================================================================


# 1. -> K vecinos más cercanos - KNN => clasificación, estima la probabilidad de que un elemento "x" pertenezca a una clase "C", a partir de la información proporcionada.

# 2. -> Árboles de decisión :  https://web.fdi.ucm.es/posgrado/conferencias/JorgeMartin-slides.pdf
# Sirven Representar y Categorizar una serie de condiciones que ocurren de forma sucesiva, para la resolución de un problema.

# 3. -> Random Forest -> Bosques Aleatorios - Algoritmo de clasificación
# combinación entre arboles de decisión en la que cada arbol selecciona una clase y luego se combinan las decisiones de cada uno para seleccionar la mejor opción.
# Maneja cientos de variables de entrada, eficiente en DB grandes

# 3. -> Máquinas de Soporte Vectorial -> SVM -> Conjunto de algoritmos de aprendizaje supervisado para resolver problemas de clasificación y regresión.
# Analizar datos y resolver patrones
# Dado un conjunto de ejemplos de entrenamiento, podemos etiquetar las clases y entrenar una SVM para construir un módelo que prediga la clase de una nueva muestra.

# Se separan las clases en dos espacios lo más amplio posible..


# 4. -> k-medias -> no supervisado, usado para clusterización
# Partición de un conjunto de "n" observaciones en "k" grupos, en el que cada observación pertenece al grupo cuyo valor medio es más cercano. - mineria de datos

# Cross Validation -O-J-O-
# 

