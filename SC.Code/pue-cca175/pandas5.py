import pandas as pd

print("----------------------------------")
input_file = "/home/hadoop/0_DEVELOP__0_DEVELOP__0_DEVELOP__/Python/PycharmProjects/pythonPUE/fichero2.csv"
df = pd.read_csv(input_file, header=0)
print(df)
"""
   number  fname     lname  age purchase  value
0       0  Jason    Miller   42        4   25.0
1       1  Molly  Jacobson   52       24   94.0
2       2   Tina         .   36       31   57.0
3       3   Jake    Milner   24        .   62.0
4       4    Amy     Cooze   73        .   70.0

"""
print("----------------------------------")
print("df.head(): ")
print(df.head())
"""
df.head(): 
   number  fname     lname  age purchase  value
0       0  Jason    Miller   42        4   25.0
1       1  Molly  Jacobson   52       24   94.0
2       2   Tina         .   36       31   57.0
3       3   Jake    Milner   24        .   62.0
4       4    Amy     Cooze   73        .   70.0
"""

print("----------------------------------")
print("df.index: ", df.index)               #   df.index:  RangeIndex(start=0, stop=5, step=1)
print("----------------------------------")
print("df.columns: ", df.columns)           #   df.columns:  Index(['number', 'fname', 'lname', 'age', 'purchase', 'value'], dtype='object')
print("----------------------------------")
print("df.values: ")
print(df.values)
"""
df.values: 
[[0 'Jason' 'Miller' 42 '4' 25.0]
 [1 'Molly' 'Jacobson' 52 '24' 94.0]
 [2 'Tina' '.' 36 '31' 57.0]
 [3 'Jake' 'Milner' 24 '.' 62.0]
 [4 'Amy' 'Cooze' 73 '.' 70.0]]
"""
print("----------------------------------")
print("df.describe: ")
print(df.describe())
"""
         number        age      value
count  5.000000   5.000000   5.000000
mean   2.000000  45.400000  61.600000
std    1.581139  18.460769  24.905823
min    0.000000  24.000000  25.000000
25%    1.000000  36.000000  57.000000
50%    2.000000  42.000000  62.000000
75%    3.000000  52.000000  70.000000
max    4.000000  73.000000  94.000000
"""