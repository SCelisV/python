# ML.py

# Machine learning => automatiza la construcción de un módelo analítico, uso de algoritmos que aprende de los datos.
# Algoritmos: Supervisado, NO Supervisado, de Refuerzo

# Supervisado => necesita datos previamente etiquetados(lo que es correcto y lo que no es correcto) para aprender a realizar el trabajo. En base a esto, el algoritmo aprenderá a resolver problemas futuros similares.
# 1. -> Regresión líneal,
# 2. -> Regresión logística
# 3. -> Máquinas de Soporte Vectorial -> SVM

# NO Supervisado => necesita indicaciones previas, No necesita datos previamente etiquetados. Aprende a comprender y a analizar la información. Práctica sobre los datos que tiene.
# 1. -> K vecinos más cercanos - KNN
# 2. -> Árboles de decisión :  https://web.fdi.ucm.es/posgrado/conferencias/JorgeMartin-slides.pdf
# 3. -> Random Forest -> Bosques Aleatorios
# 4. -> k-medias -> no supervisado, usado para clusterización

# de Refuerzo => aprende por su cuenta, en base a conocimientos introducidos previamente, aprende en función del éxito ó fracaso.

# 1. -> Regresión líneal - Supervisado - Aproximación que modela una relación entre una variable escalar dependiente ("Y") y una o más variables explicativas ("X")
# Dibujará una recta que nos indicará la tendencia del conjunto de datos, y nos ayudará a predecir en función de un valor X un valor Y.

# http://archive.ics.uci.edu/ml/datasets/Student+Performance => Student Performance => hadoop@ubuntu-hokkaido-3568:~/R/Data/workSpace/MasterR$


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
datos.19$Age
nulos <- function(Age, Pclass) {
    newAge <- Age
    for(i in 1:length(Age)){
        if( is.na(Age[i]) ) { # si es null
            if(Pclass[i] == 1){
                newAge[i] <- 33.00
            } else if(Pclass[i] == 2){
                newAge[i] <- 28.00
            } else if(Pclass[i] == 3){
                newAge[i] <- 18.00
            }   
        }        
    }
    return(newAge)
}

# Funciones con varios argumentos y aplicar el resultado a una columna
datos.19$Age <- nulos(datos.19$Age, datos.19$Pclass)


# Two Way
# creamos una función que reemplace los valores nulls del dataSet por 0, para poder calcular la media

factor(datos.19$Pclass)

nulos <- function(x) {
    #print(x)
    if( is.na(x) )
        {return (0)}
    else
        {return (x)}
}



# Three Way - Otra forma de codificar la función..
# creamos una función que reciba la edad y la clase, reemplaza los valores nulls del dataSet por la media que corresponda con la clase:
nulos <- function(x, y) {
    # x => edad => datos.19$Age
    # y => class => datos.19$Pclass
    print(x)
    print(y)
    if (y == 1){
        if( is.na(x) )
            {return (33)}
        else
            {return (x)}
    } else if (y == 2) {
            if( is.na(x) )
                {return (28)}
            else
                {return (x)}
    } else if (y == 3) {
            if( is.na(x) )
                {return (18)}
            else
                {return (x)}
    }
    else {return (x)}
}



# 1. -> K vecinos más cercanos - KNN => clasificación, estima la probabilidad de que un elemento "x" pertenezca a una clase "C", a partir de la información proporcionada.

# 2. -> Árboles de decisión :  https://web.fdi.ucm.es/posgrado/conferencias/JorgeMartin-slides.pdf
# Sirven Representar y Categorizar una serie de condiciones que ocurren de forma sucesiva, para la resolución de un problema.


# 3. -> Random Forest -> Bosques Aleatorios - Algoritmo de clasificación
# combinación entre arboles de decisión en la que cada arbol selecciona una clase y luego se combinan las decisiones de cada uno para seleccionar la mejor opción.
# Maneja cientos de variables de entrada, eficiente en DB grandes

# 3. -> Máquinas de Soporte Vectorial -> SVM -> Conjunto de algoritmos de aprendizaje supervisado para resolver problemas de clasificación y regresión.
# Analizar datos y resolver patrones
# Dado un conjunto de ejemplos de entrenamiento, podemos etiquetar las clases y entrenar una SVM para construir un modelo que prediga la clase de una nueva muestra.

# Se separan las clases en dos espacios lo más amplio posible..


# 4. -> k-medias -> no supervisado, usado para clusterización
# Partición de un conjunto de "n" observaciones en "k" grupos, en el que cada observación pertenece al grupo cuyo valor medio es más cercano. - mineria de datos



# Redes neuronales => recibir, procesar y transmitir información

# Perceptrón => neurona artificial, la unión de varios crean una red neuronal artificial.
# Se compone de:
# - Canales/Señales de entrada - Dentritas
# - Función de activación - Soma o núcleo - (unión sumadora)
# - Canal de salida y Axón.

 n
 Σ WiXi + b
i=0 

