
"""
https://pandas.pydata.org/docs/reference/index.html
# Trabajando con pandas -

# Rows - default
# axis=0 axis='rows'

# Columns
# axis=1 axis='columns'
"""

import numpy as np

datos = np.array([['', 'Col1', 'Col2'], ['fil1', 1, 2], ['fil2', 3, 4]])
print(datos)

"""
[['' 'Col1' 'Col2']
 ['fil1' '1' '2']
 ['fil2' '3' '4']]
"""

import pandas as pd
df_test = pd. DataFrame(data=datos[1:, 1:], index=datos[1:, 0], columns=datos[0, 1:])
print(df_test)
"""
    Col1 Col2
fil1    1    2
fil2    3    4
"""

# Create df from a a dictionary
songs = {
    "Album": ["Thriller", "Back in Black", "The Dark Side of the Moon",
              "The Bodyguard", "Bast Out of Hell",
              'Their Greatest Hits (1971-1975)', 'Saturday Night Fever', 'Rumours'],
    "Released": [1982, 1980, 1973, 1992, 1977, 1976, 1977, 1977],
    "Length": ["00:42:19", "00:42:22", "00:42:49", "00:57:44", "00:46:33", "", "", ""]
}

df_songs = pd.DataFrame(songs)

print(df_songs)
"""
                            Album  Released    Length
0                         Thriller      1982  00:42:19
1                    Back in Black      1980  00:42:22
2        The Dark Side of the Moon      1973  00:42:49
3                    The Bodyguard      1992  00:57:44
4                 Bast Out of Hell      1977  00:46:33
5  Their Greatest Hits (1971-1975)      1976          
6             Saturday Night Fever      1977          
7                          Rumours      1977          

"""
# https://pandas.pydata.org/docs/reference/series.html

"""
Ndarray unidimensional con las etiquetas de los ejes (incluyendo las series temporales).
Series([data, index, dtype, name, copy, …])
"""

print("np.nan: ", np.nan)   #   np.nan:  nan

serie = pd.Series([1, 3, 5, np.nan, 6, 8])
print("pd.Series([1, 3, 5, np.nan, 6, 8]): ", serie)
"""
0    1.0
1    3.0
2    5.0
3    NaN
4    6.0
5    8.0
dtype: float64

"""
s = pd.Series([1, 3, 5, np.nan, 6, 8], ['A', 'B', 'C', 'D', 'E', 'F'])
print("pd.Series([1, 3, 5, np.nan, 6, 8], ['A', 'B', 'C', 'D', 'E', 'F']): ", s)
"""
A    1.0
B    3.0
C    5.0
D    NaN
E    6.0
F    8.0
dtype: float64
"""
print("s.A: ", s.A)         # s.A:  1.0
print("s['F']: ", s['F'])   # s['F']:  8.0
print("s['B']: ", s['B'])   # s['B']:  3.0
print("s[1]: ", s[1])       # s[1]:  3.0
print("s.dtype: ", s.dtype) # s.dtype:  float64

s = pd.Series(['A', 'B', 'C', 'D', 'E', 'F'], [1, 3, 5, np.nan, 6, 8])
print("pd.Series(['A', 'B', 'C', 'D', 'E', 'F'], [1, 3, 5, np.nan, 6, 8]): ", s)
"""
1.0    A
3.0    B
5.0    C
NaN    D
6.0    E
8.0    F
dtype: object
"""
#print("s.1.0: ", s.1.0)     #   SyntaxError: invalid syntax
print("s[8.0]: ", s[8.0])   #   s[8.0]:  F
print("s[3.0]: ", s[3.0])   #   s[3.0]:  B
print("s[1]: ", s[1])       #   s[1]:  A
print("s.dtype: ", s.dtype) #   s.dtype:  object

