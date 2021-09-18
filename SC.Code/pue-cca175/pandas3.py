
"""
https://pandas.pydata.org/docs/reference/index.html
# Trabajando con pandas -

# Rows - default
# axis=0 axis='rows'

# Columns
# axis=1 axis='columns'
"""

import numpy as np
import pandas as pd
df = pd.DataFrame(np.random.randn(3, 4),  index=['2', '4', '8'],  columns=list('ABCD'))
print("df: ", df)

"""
df:            A         B         C         D
2 -0.182410  0.072852 -0.756612 -1.154884
4  1.715408 -0.372536  0.142614  0.303433
8 -0.017989  0.637437 -0.788768 -0.606752
"""

dict = {
'A' : 1.,
'B' : pd.Timestamp('20130102'),
'C' : pd.Series(1, index=list(range(4)), dtype='float32'),
'D' : np.array([3] * 4, dtype='int32'),
'E' : pd.Categorical(["test", "train", "test", "train"]),
'F' : 'foo'
}

df = pd.DataFrame(dict)
print("df: ")           #   df:
print(df)
"""
df: 
     A          B    C  D      E    F
0  1.0 2013-01-02  1.0  3   test  foo
1  1.0 2013-01-02  1.0  3  train  foo
2  1.0 2013-01-02  1.0  3   test  foo
3  1.0 2013-01-02  1.0  3  train  foo
"""

print("df.dtypes: ")        # df.dtypes:
print(df.dtypes)
"""
A           float64
B    datetime64[ns]
C           float32
D             int32
E          category
F            object
dtype: object
"""
