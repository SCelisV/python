import pandas as pd
print("----------------------------------")
fichero = "/home/hadoop/0_DEVELOP__0_DEVELOP__0_DEVELOP__/Python/PycharmProjects/pythonPUE/files/fichero.csv"
df = pd.read_csv(fichero)
print(df)
print("\ndf.head(): ", df.head())
"""
   0  Jason    Miller  42   4  25.000
0  1  Molly  Jacobson  52  24    94.0
1  2   Tina         .  36  31    57.0
2  3   Jake    Milner  24   .    62.0
3  4    Amy     Cooze  73   .    70.0

df.head():     0  Jason    Miller  42   4  25.000
"""
print("----------------------------------")
input_file = "/home/hadoop/0_DEVELOP__0_DEVELOP__0_DEVELOP__/Python/PycharmProjects/pythonPUE/files/fichero.csv"
df = pd.read_csv(input_file, header=0)
print(df)
"""
   0  Jason    Miller  42   4  25.000
0  1  Molly  Jacobson  52  24    94.0
1  2   Tina         .  36  31    57.0
2  3   Jake    Milner  24   .    62.0
3  4    Amy     Cooze  73   .    70.0

"""
print("----------------------------------")
print("df.head(): ")
print(df.head())
"""
   0  Jason    Miller  42   4  25.000
0  1  Molly  Jacobson  52  24    94.0
1  2   Tina         .  36  31    57.0
2  3   Jake    Milner  24   .    62.0
3  4    Amy     Cooze  73   .    70.0
"""
print("----------------------------------")
import numpy as np
df = pd.DataFrame(np.random.randn(10, 4), columns=list('ABCD'))
print(df.head())

"""
          A         B         C         D
0 -2.434318 -0.739137 -0.196021  0.163697
1 -2.749857 -0.588852 -0.179378  0.224139
2 -0.240269 -1.323488 -0.562511  0.096547
3  0.170110  1.385341  0.678920  0.258124
4 -0.473398  0.639965 -0.018005 -1.880093
"""
print("----------------------------------")
print(df.tail(2))
"""
          A         B         C         D
8 -0.499623  0.288755  0.326203 -0.462029
9 -0.145652  0.879865  0.703253  0.219132
"""
print("----------------------------------")
print("df.index: ", df.index)               # df.index:  RangeIndex(start=0, stop=10, step=1)
print("----------------------------------")
print("df.columns: ", df.columns)           # df.columns:  Index(['A', 'B', 'C', 'D'], dtype='object')
print("----------------------------------")
print("df.values: ", df.values)
"""
[[-2.43431778 -0.73913745 -0.19602059  0.16369729]
 [-2.74985748 -0.58885172 -0.17937787  0.22413887]
 [-0.24026926 -1.32348772 -0.56251142  0.09654719]
 [ 0.17010973  1.38534143  0.67892043  0.2581236 ]
 [-0.47339846  0.63996488 -0.01800464 -1.88009343]
 [-0.86945928  1.88185718  0.31370817 -0.37853139]
 [-1.3467676  -0.36816869 -0.35505954  0.75772515]
 [-1.69060263  0.0568047  -1.20947887  0.65465524]
 [-0.49962311  0.28875506  0.32620277 -0.46202873]
 [-0.14565164  0.87986532  0.70325276  0.21913217]]
"""
