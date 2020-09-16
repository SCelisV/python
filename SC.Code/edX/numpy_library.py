#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IN-WORK-OUT
Created on Fri Aug 21 19:33:55 2020

@author: SCELIS
# numpy_library.py - for arrays and operations with arrays
A numpy array is similar to a list. 
It's usually fixed in size and each element is of the same type. 
https://numpy.org

"""

import numpy as np

# devuelven muestras numéricamente espaciadas, calculadas sobre el intervalo
X_plot = np.linspace(0,40) # ordenados por fila 
print(X_plot)
X_plot = np.linspace(0,40).reshape(-1, 1) # ordenados por columna
print(X_plot)

# create an py array - has an index start on 0 are differents types
a=["0", 1, "two", "3", 4]
type(a) # list

# TypeError: list indices must be integers or slices, not str
# for i in a:
#     print ("position: ", i ,",", a[i])


# can cast a list to a numpy array 
a=np.array(["0", 1, "two", "3", 4])

# create an numpy array or ndarray - the elements has the same type
# numpy arrays contain data of the same type
a=[0,1,2,3,4]
type(a) # list

for i in a:
    print ("position: a[", i ,"]: ", a[i])
    
# position: a[ 0 ]:  0
# position: a[ 1 ]:  1
# position: a[ 2 ]:  2
# position: a[ 3 ]:  3
# position: a[ 4 ]:  4

# we can cast a list to a numpy array ndarray
a=np.array([0,1,2,3,4])
type(a) # numpy.ndarray # tipo de objeto

z=np.array([20, 1, 2, 3, 4])
# can use a list to select a specific index
# Create the index list
select = [0, 2, 3]
w = z[select]
w # array([20,  2,  3])

# Assign the specified elements to new value - change
z[select] = 5
z # array([5, 1, 5, 5, 4])

# obtain data-type of the array's elements - tipo de los elementos del array
a.dtype # dtype('int64') 64-bit integer

dir(a)
# total of elements in the array like len
a.size # 5

len(a) # 5

#number or array dimensions of the rank of the array
a.ndim # 1

# the shape (tamaño) of the array, tupla de integers indicating the size of the array in each dimensions 
print(a.shape) 
a.shape # (5,)

b=np.array([3.1,11.02,6.2,213.2,5.2])
type(b) # numpy.ndarray
b.dtype # dtype('float64') 64-bit float

# Indexing and Slicing (cortar)

c=np.array([20,1,2,3,4])
# change an element of array
c[0]=100
c #array([100,   1,   2,   3,   4])

# Slicing (cortar) the elements 1 to 3
d=c[1:4]
d # array([1, 2, 3])
type(d) # numpy.ndarray

# change new vales using the corresponding indexes
c[2:5] # corresponde a las posiciones array([2, 3, 4]) del array

# c[2:5]=300,400 
# ValueError: cannot copy sequence with size 2 to array axis with dimension 3

c[2:5]=300,400,100
c # array([100,   1, 300, 400, 100])

# Basic Operations
# array add(+) and subtrac(-) (suma, resta)

u=np.array([1,0]) # array([1, 0]) # (x, y) # (horizontal, vertical)
v=np.array([0,1]) # array([0, 1]) # (x, y) # (horizontal, vertical)

z=u+v
z # array([1, 1]) # (x, y) # (horizontal, vertical)
type(z) # numpy.ndarray
dir (z)
y=u-v
y # array([ 1, -1])
type(y) # numpy.ndarray

# -------------------------

u=[1,0] #  [1, 0] # (x, y) # (horizontal, vertical)
type(u) # list
dir (u)

v=[0,1]

# si no se crea el arreglo genera un error
# AttributeError: 'numpy.ndarray' object has no attribute 'append'
z=[]

for n, m in zip(u,v): 
    z.append(n+m)
    
z # [1, 1]

type(z) # list
dir (z)    
# -------------------------

z=[]
for n, m in zip(u,v): 
    z.append(n-m)

z # [1, -1]

type(z) # list
dir (z)   
 
# -------------------------

# array multiplication with a Scalar 

y = [1,2]

# z = 2y 
# sería [2*1,2*2]

y = np.array([1,2])
z = 2*y
z # array([2, 4])
type(z) # numpy.ndarray

y=[1,2]
z=[]
for n in y: 
    z.append(2*n)

z # [2, 4]

type(z) # list
dir (z) 

# Product of two numpy arrays

u=np.array([1,2]) # 
v=np.array([3,2]) # 

z=u*v
z # array([3, 4])
type(z) # numpy.ndarray
dir (z)

u = [1,2]
v = [3,2]
z=[]

for n, m in zip(u,v): 
    z.append(n*m)
    
z # [3, 4]

type(z) # list
dir (z)    


# Dot Product of two numpy arrays, how similar two arrays are.
# https://numpy.org/doc/stable/reference/generated/numpy.dot.html

u = [1,2]
v = [3,1]
# uTv =  [1*3] + [2*1] = 5 
# representa si los vectores son similares

u=np.array([1,2]) # 
v=np.array([3,1]) # 

result = np.dot(u,v)
result # 5
type(result) # numpy.int64

np.dot(np.array([1,-1]),np.array([1,1])) 
# [1*1]+[-1*1]
# 1-1
# 0

np.dot(3, 4)
# 12

# Ninguno de los dos argumentos es complejo
np.dot([2j, 3j], [2j, 3j])
# [2j*2j]+[3j*3j]
# 4+9
(-13+0j)

# For 2-D arrays it is the matrix product
a = [[1, 0], [0, 1]]
b = [[4, 1], [2, 2]]

np.dot(a, b)

# 
# array([[4, 1],
#        [2, 2]])

# the matrix product
# MatrizA  -  MatrizB  =      Resultado

#   e, f   -   a, b    =  e*a + f*c + e*b + f*d
#   g, h   -   c, d       g*a + h*c + g*b + h*d

# Adding Constant to an numpy Array (broadcasting)

u=np.array([1,2,3,-1]) # [1+1,2+1,3+1,-1+1]
z=u+1
z # array([2, 3, 4, 0])
type(z) # numpy.ndarray

# Universal Functions - a function that operates on ndarrays

a=np.array([1,-1,1,-1])

# media - average
mean_a = a.mean()
mean_a # 0.0

# desviación standard
desv = a.std()
desv # 1.0

b=np.array([1,-2,3,4,5])

# max - máximo
max_b = b.max()
max_b # 5

# min - mínimo
min_b = b.min()
min_b # -2

np.pi # 3.141592653589793

x=np.array([0,np.pi/2,np.pi]) 
x # array([0.        , 1.57079633, 3.14159265])
type(x) # numpy.ndarray
dir(x)

y = np.sin(x)  # =>[sin(0),sin(np.pi/2),sin(np.pi)]
y # array([0.0000000e+00, 1.0000000e+00, 1.2246468e-16])
type(y)

# return evenly spaced numbers over a specified interval. 
# devuelven números uniformemente espaciados a lo largo de un intervalo especificado

# (-2) the starting point of the sequence (secuencia)
# (2) the ending point of sequence 
# (num=5) the number of samples to generate

np.linspace(-2,2,num=5) # array([-2., -1.,  0.,  1.,  2.])
np.linspace(-2,2,num=9) # array([-2. , -1.5, -1. , -0.5,  0. ,  0.5,  1. ,  1.5,  2. ])

# Plotting Mathematical Functions

# linspace use for generate 100 evenly spaced samples from the interval 0 to 2pi.
x=np.linspace(0,2*np.pi,100)
x
# array([0.        , 0.06346652, 0.12693304, 0.19039955, 0.25386607,
#        0.31733259, 0.38079911, 0.44426563, 0.50773215, 0.57119866,
#        0.63466518, 0.6981317 , 0.76159822, 0.82506474, 0.88853126,
#        0.95199777, 1.01546429, 1.07893081, 1.14239733, 1.20586385,
#        1.26933037, 1.33279688, 1.3962634 , 1.45972992, 1.52319644,
#        1.58666296, 1.65012947, 1.71359599, 1.77706251, 1.84052903,
#        1.90399555, 1.96746207, 2.03092858, 2.0943951 , 2.15786162,
#        2.22132814, 2.28479466, 2.34826118, 2.41172769, 2.47519421,
#        2.53866073, 2.60212725, 2.66559377, 2.72906028, 2.7925268 ,
#        2.85599332, 2.91945984, 2.98292636, 3.04639288, 3.10985939,
#        3.17332591, 3.23679243, 3.30025895, 3.36372547, 3.42719199,
#        3.4906585 , 3.55412502, 3.61759154, 3.68105806, 3.74452458,
#        3.8079911 , 3.87145761, 3.93492413, 3.99839065, 4.06185717,
#        4.12532369, 4.1887902 , 4.25225672, 4.31572324, 4.37918976,
#        4.44265628, 4.5061228 , 4.56958931, 4.63305583, 4.69652235,
#        4.75998887, 4.82345539, 4.88692191, 4.95038842, 5.01385494,
#        5.07732146, 5.14078798, 5.2042545 , 5.26772102, 5.33118753,
#        5.39465405, 5.45812057, 5.52158709, 5.58505361, 5.64852012,
#        5.71198664, 5.77545316, 5.83891968, 5.9023862 , 5.96585272,
#        6.02931923, 6.09278575, 6.15625227, 6.21971879, 6.28318531])
# use the numpy functions to map the array x to new array y
y=np.sin(x)
y
# array([ 0.00000000e+00,  6.34239197e-02,  1.26592454e-01,  1.89251244e-01,
#         2.51147987e-01,  3.12033446e-01,  3.71662456e-01,  4.29794912e-01,
#         4.86196736e-01,  5.40640817e-01,  5.92907929e-01,  6.42787610e-01,
#         6.90079011e-01,  7.34591709e-01,  7.76146464e-01,  8.14575952e-01,
#         8.49725430e-01,  8.81453363e-01,  9.09631995e-01,  9.34147860e-01,
#         9.54902241e-01,  9.71811568e-01,  9.84807753e-01,  9.93838464e-01,
#         9.98867339e-01,  9.99874128e-01,  9.96854776e-01,  9.89821442e-01,
#         9.78802446e-01,  9.63842159e-01,  9.45000819e-01,  9.22354294e-01,
#         8.95993774e-01,  8.66025404e-01,  8.32569855e-01,  7.95761841e-01,
#         7.55749574e-01,  7.12694171e-01,  6.66769001e-01,  6.18158986e-01,
#         5.67059864e-01,  5.13677392e-01,  4.58226522e-01,  4.00930535e-01,
#         3.42020143e-01,  2.81732557e-01,  2.20310533e-01,  1.58001396e-01,
#         9.50560433e-02,  3.17279335e-02, -3.17279335e-02, -9.50560433e-02,
#        -1.58001396e-01, -2.20310533e-01, -2.81732557e-01, -3.42020143e-01,
#        -4.00930535e-01, -4.58226522e-01, -5.13677392e-01, -5.67059864e-01,
#        -6.18158986e-01, -6.66769001e-01, -7.12694171e-01, -7.55749574e-01,
#        -7.95761841e-01, -8.32569855e-01, -8.66025404e-01, -8.95993774e-01,
#        -9.22354294e-01, -9.45000819e-01, -9.63842159e-01, -9.78802446e-01,
#        -9.89821442e-01, -9.96854776e-01, -9.99874128e-01, -9.98867339e-01,
#        -9.93838464e-01, -9.84807753e-01, -9.71811568e-01, -9.54902241e-01,
#        -9.34147860e-01, -9.09631995e-01, -8.81453363e-01, -8.49725430e-01,
#        -8.14575952e-01, -7.76146464e-01, -7.34591709e-01, -6.90079011e-01,
#        -6.42787610e-01, -5.92907929e-01, -5.40640817e-01, -4.86196736e-01,
#        -4.29794912e-01, -3.71662456e-01, -3.12033446e-01, -2.51147987e-01,
#        -1.89251244e-01, -1.26592454e-01, -6.34239197e-02, -2.44929360e-16])
# can import the library pyplot as plt to help us plot the function.
# in (ipynb) => %matplotlib inline to display the plot.

import matplotlib.pyplot as plt
# %matplotlib inline  
# plots a graph.

plt.plot(x,y)
# (x are the values for the horizontal or x-axis)
# (y are the values for the vertical or y-axis)

# Import the libraries

import numpy as np 

import matplotlib.pyplot as plt

# Plotting functions

def Plotvec1(u, z, v):
    
    ax = plt.axes()
    ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)
    plt.text(*(u + 0.1), 'u')
    
    ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)
    plt.text(*(v + 0.1), 'v')
    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z + 0.1), 'z')
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)

def Plotvec2(a,b):
    ax = plt.axes()
    ax.arrow(0, 0, *a, head_width=0.05, color ='r', head_length=0.1)
    plt.text(*(a + 0.1), 'a')
    ax.arrow(0, 0, *b, head_width=0.05, color ='b', head_length=0.1)
    plt.text(*(b + 0.1), 'b')
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)

u = np.array([1, 0])
u

v = np.array([0, 1])
v

z = u + v
z

Plotvec1(u, z, v)

a=np.array([-1, 1])
b=np.array([1, 1])
Plotvec2(a,b)
print("The dot product is:", np.dot(a,b))

a=np.array([1, 0])
b=np.array([0, 1])
Plotvec2(a,b)
print("The dot product is:", np.dot(a,b))

a=np.array([1, 1]) 
b=np.array([0, 1])
Plotvec2(a,b)
print("The dot product is:", np.dot(a,b))

# Why are the results of the dot product for [-1, 1] and [1, 1] and the dot product for [1, 0] and [0, 1] zero, but not zero for the dot product for [1, 1] and [0, 1]?
# Hint: Study the corresponding figures, pay attention to the direction the arrows are pointing to.
# R:/
# The vectors used for question ([-1, 1] and [1, 1]) and ([1, 0] and [0, 1]) are perpendicular. 
# As a result, the dot product is zero.

# numpy 2D - Matriz

a=[[11,12,13],[21,22,23],[31,32,33]]

# cast A=np.array([[11,12,13],[21,22,23],[31,32,33]]) ó
A=np.array(a)
# array([[11, 12, 13],
#        [21, 22, 23],
#        [31, 32, 33]])

# obtain the number of axes or dimensions referred to as the rank. 
# ver los [], cada par es una dimensión
# A=np.array( [[11,12,13],[21,22,23],[31,32,33]] ) => ndim = 2
# A=np.array([[[11,12,13],[21,22,23],[31,32,33]]]) => ndim = 3
# Rank does not refer to the number of linearly independent columns like a Matriz 
# It's useful to think of "ndim" as the number of nested - (anidadas) list
A.ndim # 2

# The number of lists the list contains doesn't have to do with the dimension but the shape of the list
# returns a tuple corresponding to the size or number of each dimension
# As with the 1D array, the attribute "shape" returns a tuple
# It's helpful to use the rectangular representation as well
# The first element in the tuple corresponds to the number of nested list contained in the original list or the number of rows.
# The second element corresponds to the size of each of the nested lists or the number of colums in the rectangular array 0.
# axis0 - vertical
# axis 1 - horizontal
A.shape # (3, 3)

# The number of elements 3 rows * 3 columns
A.size # 9

#  __0__1__2
# 0|11 12 13
# 1|21 22 23
# 2|31 32 33


# Acces the differents elements of the array A[0][0], A[row][col]
# A: [[A[0][0],A[0][1],A[0][2]], [A[1][0],A[1][1],A[1][2]], [A[2][0],A[2][1],A[2][2]]]

A[0][0] # 11
A[0, 0] # 11
A[1][2] # 23
A[1, 2] # 23

# slicing (cortar) in numpy arrays
A[0][0:2] # array([11, 12])
A[0, 0:2] # A[row0, 2col(0 y 1)] - array([11, 12]), 

A[0:2, 2] # array([13, 23])
A[0:2, 2] # A[2rows(0 y 1), Col2] - array([13, 23])

#  _0_1
# 0|1 0
# 1|0 1

# sum two matriz rows = cols
X = np.array( [[1,0],[0,1]] )
# array([[1, 0],
#        [0, 1]])
Y = np.array( [[2,1],[1,2]] )
# array([[2, 1],
#        [1, 2]])
Z = X+Y
type(Z) # numpy.ndarray
# array([[3, 1],
#        [1, 3]])

# multiplay by scalar number
Z = Y*2
Z
# array([[4, 2],
#        [2, 4]])

# multiplay two arrays - producto de los elementos o producto Hadamard 
# multiply each of the elements in the same position
# The result is a new matrix that is the same size as matrix Y or X

Z = X*Y
Z
# array([[2, 0],
#        [0, 2]])

# multiply two matriz - the dot product
A = np.array( [[0,1,1],[1,0,1]] )
B = np.array( [[1,1],[1,1],[-1,1]] )

C = np.dot(A,B) # Algebraicamente the number colums A = the number filas B
C
# array([[0, 2],
#        [0, 2]])
# irow and jcolum = dot product of the irow of A whith the j columns of B

# A__0__1__2
# 0| 0  1  1
# 1| 1  0  1


# B__0__1
# 0| 1  1
# 1| 1  1
# 2|-1  1

# A * B 
# ___0__1
# 0| 0  2
# 1| 0  2

# A[0][0]*B[0][0] + A[0][1]*B[1][0] + A[0][2]*B[2][0] = 0
# A[0][0]*B[0][1] + A[0][1]*B[1][1] + A[0][2]*B[2][1] = 2
# A[1][0]*B[0][0] + A[1][1]*B[1][0] + A[1][2]*B[2][0] = 0
# A[1][0]*B[0][1] + A[1][1]*B[1][1] + A[1][2]*B[2][1] = 2

# aplicando una function sen
np.sin(C)
# array([[0.        , 0.90929743],
#        [0.        , 0.90929743]])


C = np.array([[1,1],[2,2],[3,3]])
C
# array([[1, 1],
#        [2, 2],
#        [3, 3]])
C.shape # (3, 2)

# attribute T to calculate the transposed matrix
# Get the transposed of C
D = C.T
D
# array([[1, 2, 3],
#        [1, 2, 3]])
D.shape # (2, 3)


A=np.array([[1,2],[3,4],[5,6],[7,8]])
A.shape # (4, 2)