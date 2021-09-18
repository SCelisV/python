"""
https://pandas.pydata.org/docs/reference/index.html
"""
import numpy as np
import pandas as pd

datos = np.array([1, 2, 3, 4, 5, 6, 7])
print("datos: ", datos)         #   datos:  [1 2 3 4 5 6 7]

df = pd.DataFrame(datos)
print("df: ", df)
"""
df:     0
0  1
1  2
2  3
3  4
4  5
5  6
6  7
"""

data = np.array([['', 'Col1', 'Col2'], ['Row1', 1, 2], ['Row2', 3, 4]])
print("data: ", data)
"""
data:  
[['' 'Col1' 'Col2']
 ['Row1' '1' '2']
 ['Row2' '3' '4']]
"""
df = pd.DataFrame(data=data[1:, 1:], index=data[1:, 0], columns=data[0, 1:])
print("df: ", df)
"""
df:       Col1 Col2
Row1    1    2
Row2    3    4
"""
