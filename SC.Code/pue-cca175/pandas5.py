import pandas as pd

print("----------------------------------")
input_file = "/home/hadoop/0_DEVELOP__0_DEVELOP__0_DEVELOP__/Python/PycharmProjects/pythonPUE/files/fichero2.csv"
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
print("----------------------------------")
# Display an array with head and tail
df.to_numpy()
"""
array([[0, 'Jason', 'Miller', 42, '4', 25.0],
       [1, 'Molly', 'Jacobson', 52, '24', 94.0],
       [2, 'Tina', '.', 36, '31', 57.0],
"""
print("----------------------------------")
print("df.dtypes:\n", df.dtypes)
"""
df.dtypes: 
number        int64
fname        object
lname        object
age           int64
purchase     object
value       float64
dtype: object
----------------------------------
"""
print("----------------------------------")
print("df.info:\n", df.info)
print("----------------------------------")
print("dir(df):\n", dir(df))
print("----------------------------------")


# Get the column as a dataframe - Crea un dataframe de una columna del dframe
x = (df[['fname']])

print("crea un dataframe de una columna del frame - x = (df[['fname']]):\n", x)

print("type(x): ", type(x))
x       # pandas.core.frame.DataFrame

print("dir (x): ", dir(x))
# dir (x):  ['T', '_AXIS_LEN', '_AXIS_ORDERS', '_AXIS_REVERSED', '_AXIS_TO_AXIS_NUMBER', '_HANDLED_TYPES', '__abs__', '__add__', '__and__', '__annotations__', '__array__', '__array_priority__', '__array_ufunc__', '__array_wrap__', '__bool__', '__class__', '__contains__', '__copy__', '__deepcopy__', '__delattr__', '__delitem__', '__dict__', '__dir__', '__divmod__', '__doc__', '__eq__', '__finalize__', '__floordiv__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__iand__', '__ifloordiv__', '__imod__', '__imul__', '__init__', '__init_subclass__', '__invert__', '__ior__', '__ipow__', '__isub__', '__iter__', '__itruediv__', '__ixor__', '__le__', '__len__', '__lt__', '__matmul__', '__mod__', '__module__', '__mul__', '__ne__', '__neg__', '__new__', '__nonzero__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmatmul__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__setitem__', '__setstate__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__weakref__', '__xor__', '_accessors', '_accum_func', '_add_numeric_operations', '_agg_by_level', '_agg_examples_doc', '_agg_summary_and_see_also_doc', '_align_frame', '_align_series', '_arith_method', '_as_manager', '_attrs', '_box_col_values', '_can_fast_transpose', '_check_inplace_and_allows_duplicate_labels', '_check_inplace_setting', '_check_is_chained_assignment_possible', '_check_label_or_level_ambiguity', '_check_setitem_copy', '_clear_item_cache', '_clip_with_one_bound', '_clip_with_scalar', '_cmp_method', '_combine_frame', '_consolidate', '_consolidate_inplace', '_construct_axes_dict', '_construct_axes_from_arguments', '_construct_result', '_constructor', '_constructor_sliced', '_convert', '_count_level', '_data', '_dir_additions', '_dir_deletions', '_dispatch_frame_op', '_drop_axis', '_drop_labels_or_levels', '_ensure_valid_index', '_find_valid_index', '_flags', '_from_arrays', '_from_mgr', '_get_agg_axis', '_get_axis', '_get_axis_name', '_get_axis_number', '_get_axis_resolvers', '_get_block_manager_axis', '_get_bool_data', '_get_cleaned_column_resolvers', '_get_column_array', '_get_index_resolvers', '_get_item_cache', '_get_label_or_level_values', '_get_numeric_data', '_get_value', '_getitem_bool_array', '_getitem_multilevel', '_gotitem', '_hidden_attrs', '_indexed_same', '_info_axis', '_info_axis_name', '_info_axis_number', '_info_repr', '_init_mgr', '_inplace_method', '_internal_names', '_internal_names_set', '_is_copy', '_is_homogeneous_type', '_is_label_or_level_reference', '_is_label_reference', '_is_level_reference', '_is_mixed_type', '_is_view', '_iset_item', '_iset_item_mgr', '_iset_not_inplace', '_item_cache', '_iter_column_arrays', '_ixs', '_join_compat', '_logical_func', '_logical_method', '_maybe_cache_changed', '_maybe_update_cacher', '_metadata', '_mgr', '_min_count_stat_function', '_needs_reindex_multi', '_protect_consolidate', '_reduce', '_reindex_axes', '_reindex_columns', '_reindex_index', '_reindex_multi', '_reindex_with_indexers', '_replace_columnwise', '_repr_data_resource_', '_repr_fits_horizontal_', '_repr_fits_vertical_', '_repr_html_', '_repr_latex_', '_reset_cache', '_reset_cacher', '_sanitize_column', '_series', '_set_axis', '_set_axis_name', '_set_axis_nocheck', '_set_is_copy', '_set_item', '_set_item_frame_value', '_set_item_mgr', '_set_value', '_setitem_array', '_setitem_frame', '_setitem_slice', '_slice', '_stat_axis', '_stat_axis_name', '_stat_axis_number', '_stat_function', '_stat_function_ddof', '_take_with_is_copy', '_to_dict_of_blocks', '_typ', '_update_inplace', '_validate_dtype', '_values', '_where', 'abs', 'add', 'add_prefix', 'add_suffix', 'agg', 'aggregate', 'align', 'all', 'any', 'append', 'apply', 'applymap', 'asfreq', 'asof', 'assign', 'astype', 'at', 'at_time', 'attrs', 'axes', 'backfill', 'between_time', 'bfill', 'bool', 'boxplot', 'clip', 'columns', 'combine', 'combine_first', 'compare', 'convert_dtypes', 'copy', 'corr', 'corrwith', 'count', 'cov', 'cummax', 'cummin', 'cumprod', 'cumsum', 'describe', 'diff', 'div', 'divide', 'dot', 'drop', 'drop_duplicates', 'droplevel', 'dropna', 'dtypes', 'duplicated', 'empty', 'eq', 'equals', 'eval', 'ewm', 'expanding', 'explode', 'ffill', 'fillna', 'filter', 'first', 'first_valid_index', 'flags', 'floordiv', 'fname', 'from_dict', 'from_records', 'ge', 'get', 'groupby', 'gt', 'head', 'hist', 'iat', 'idxmax', 'idxmin', 'iloc', 'index', 'infer_objects', 'info', 'insert', 'interpolate', 'isin', 'isna', 'isnull', 'items', 'iteritems', 'iterrows', 'itertuples', 'join', 'keys', 'kurt', 'kurtosis', 'last', 'last_valid_index', 'le', 'loc', 'lookup', 'lt', 'mad', 'mask', 'max', 'mean', 'median', 'melt', 'memory_usage', 'merge', 'min', 'mod', 'mode', 'mul', 'multiply', 'ndim', 'ne', 'nlargest', 'notna', 'notnull', 'nsmallest', 'nunique', 'pad', 'pct_change', 'pipe', 'pivot', 'pivot_table', 'plot', 'pop', 'pow', 'prod', 'product', 'quantile', 'query', 'radd', 'rank', 'rdiv', 'reindex', 'reindex_like', 'rename', 'rename_axis', 'reorder_levels', 'replace', 'resample', 'reset_index', 'rfloordiv', 'rmod', 'rmul', 'rolling', 'round', 'rpow', 'rsub', 'rtruediv', 'sample', 'select_dtypes', 'sem', 'set_axis', 'set_flags', 'set_index', 'shape', 'shift', 'size', 'skew', 'slice_shift', 'sort_index', 'sort_values', 'squeeze', 'stack', 'std', 'style', 'sub', 'subtract', 'sum', 'swapaxes', 'swaplevel', 'tail', 'take', 'to_clipboard', 'to_csv', 'to_dict', 'to_excel', 'to_feather', 'to_gbq', 'to_hdf', 'to_html', 'to_json', 'to_latex', 'to_markdown', 'to_numpy', 'to_parquet', 'to_period', 'to_pickle', 'to_records', 'to_sql', 'to_stata', 'to_string', 'to_timestamp', 'to_xarray', 'to_xml', 'transform', 'transpose', 'truediv', 'truncate', 'tz_convert', 'tz_localize', 'unstack', 'update', 'value_counts', 'values', 'var', 'where', 'xs']

# Get the column as a series - Crea una serie de una columna del dframe
x = df['age']
print("Crea una serie de una columna del dframe - x = df['age']:\n", x)
"""
0    42
1    52
2    36
3    24
4    73
Name: age, dtype: int64
"""
print("type(x): ", type(x))     # <class 'pandas.core.series.Series'>

print("dir(x): ", dir(x))   #    ['T', '_AXIS_LEN', '_AXIS_ORDERS', '_AXIS_REVERSED', '_AXIS_TO_AXIS_NUMBER', '_HANDLED_TYPES', '__abs__', '__add__', '__and__', '__annotations__', '__array__', '__array_priority__', '__array_ufunc__', '__array_wrap__', '__bool__', '__class__', '__contains__', '__copy__', '__deepcopy__', '__delattr__', '__delitem__', '__dict__', '__dir__', '__divmod__', '__doc__', '__eq__', '__finalize__', '__float__', '__floordiv__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__iand__', '__ifloordiv__', '__imod__', '__imul__', '__init__', '__init_subclass__', '__int__', '__invert__', '__ior__', '__ipow__', '__isub__', '__iter__', '__itruediv__', '__ixor__', '__le__', '__len__', '__long__', '__lt__', '__matmul__', '__mod__', '__module__', '__mul__', '__ne__', '__neg__', '__new__', '__nonzero__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmatmul__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__setitem__', '__setstate__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__weakref__', '__xor__', '_accessors', '_accum_func', '_add_numeric_operations', '_agg_by_level', '_agg_examples_doc', '_agg_see_also_doc', '_align_frame', '_align_series', '_arith_method', '_as_manager', '_attrs', '_binop', '_cacher', '_can_hold_na', '_check_inplace_and_allows_duplicate_labels', '_check_inplace_setting', '_check_is_chained_assignment_possible', '_check_label_or_level_ambiguity', '_check_setitem_copy', '_clear_item_cache', '_clip_with_one_bound', '_clip_with_scalar', '_cmp_method', '_consolidate', '_consolidate_inplace', '_construct_axes_dict', '_construct_axes_from_arguments', '_construct_result', '_constructor', '_constructor_expanddim', '_convert', '_convert_dtypes', '_data', '_dir_additions', '_dir_deletions', '_drop_axis', '_drop_labels_or_levels', '_duplicated', '_find_valid_index', '_flags', '_from_mgr', '_get_axis', '_get_axis_name', '_get_axis_number', '_get_axis_resolvers', '_get_block_manager_axis', '_get_bool_data', '_get_cacher', '_get_cleaned_column_resolvers', '_get_index_resolvers', '_get_label_or_level_values', '_get_numeric_data', '_get_value', '_get_values', '_get_values_tuple', '_get_with', '_gotitem', '_hidden_attrs', '_index', '_indexed_same', '_info_axis', '_info_axis_name', '_info_axis_number', '_init_dict', '_init_mgr', '_inplace_method', '_internal_names', '_internal_names_set', '_is_cached', '_is_copy', '_is_label_or_level_reference', '_is_label_reference', '_is_level_reference', '_is_mixed_type', '_is_view', '_item_cache', '_ixs', '_logical_func', '_logical_method', '_map_values', '_maybe_update_cacher', '_memory_usage', '_metadata', '_mgr', '_min_count_stat_function', '_name', '_needs_reindex_multi', '_protect_consolidate', '_reduce', '_reindex_axes', '_reindex_indexer', '_reindex_multi', '_reindex_with_indexers', '_replace_single', '_repr_data_resource_', '_repr_latex_', '_reset_cache', '_reset_cacher', '_set_as_cached', '_set_axis', '_set_axis_name', '_set_axis_nocheck', '_set_is_copy', '_set_labels', '_set_name', '_set_value', '_set_values', '_set_with', '_set_with_engine', '_slice', '_stat_axis', '_stat_axis_name', '_stat_axis_number', '_stat_function', '_stat_function_ddof', '_take_with_is_copy', '_typ', '_update_inplace', '_validate_dtype', '_values', '_where', 'abs', 'add', 'add_prefix', 'add_suffix', 'agg', 'aggregate', 'align', 'all', 'any', 'append', 'apply', 'argmax', 'argmin', 'argsort', 'array', 'asfreq', 'asof', 'astype', 'at', 'at_time', 'attrs', 'autocorr', 'axes', 'backfill', 'between', 'between_time', 'bfill', 'bool', 'clip', 'combine', 'combine_first', 'compare', 'convert_dtypes', 'copy', 'corr', 'count', 'cov', 'cummax', 'cummin', 'cumprod', 'cumsum', 'describe', 'diff', 'div', 'divide', 'divmod', 'dot', 'drop', 'drop_duplicates', 'droplevel', 'dropna', 'dtype', 'dtypes', 'duplicated', 'empty', 'eq', 'equals', 'ewm', 'expanding', 'explode', 'factorize', 'ffill', 'fillna', 'filter', 'first', 'first_valid_index', 'flags', 'floordiv', 'ge', 'get', 'groupby', 'gt', 'hasnans', 'head', 'hist', 'iat', 'idxmax', 'idxmin', 'iloc', 'index', 'infer_objects', 'interpolate', 'is_monotonic', 'is_monotonic_decreasing', 'is_monotonic_increasing', 'is_unique', 'isin', 'isna', 'isnull', 'item', 'items', 'iteritems', 'keys', 'kurt', 'kurtosis', 'last', 'last_valid_index', 'le', 'loc', 'lt', 'mad', 'map', 'mask', 'max', 'mean', 'median', 'memory_usage', 'min', 'mod', 'mode', 'mul', 'multiply', 'name', 'nbytes', 'ndim', 'ne', 'nlargest', 'notna', 'notnull', 'nsmallest', 'nunique', 'pad', 'pct_change', 'pipe', 'plot', 'pop', 'pow', 'prod', 'product', 'quantile', 'radd', 'rank', 'ravel', 'rdiv', 'rdivmod', 'reindex', 'reindex_like', 'rename', 'rename_axis', 'reorder_levels', 'repeat', 'replace', 'resample', 'reset_index', 'rfloordiv', 'rmod', 'rmul', 'rolling', 'round', 'rpow', 'rsub', 'rtruediv', 'sample', 'searchsorted', 'sem', 'set_axis', 'set_flags', 'shape', 'shift', 'size', 'skew', 'slice_shift', 'sort_index', 'sort_values', 'squeeze', 'std', 'sub', 'subtract', 'sum', 'swapaxes', 'swaplevel', 'tail', 'take', 'to_clipboard', 'to_csv', 'to_dict', 'to_excel', 'to_frame', 'to_hdf', 'to_json', 'to_latex', 'to_list', 'to_markdown', 'to_numpy', 'to_period', 'to_pickle', 'to_sql', 'to_string', 'to_timestamp', 'to_xarray', 'transform', 'transpose', 'truediv', 'truncate', 'tz_convert', 'tz_localize', 'unique', 'unstack', 'update', 'value_counts', 'values', 'var', 'view', 'where', 'xs']

print("sql_distinct, determine the unique elementos in a column of a dataframe - x.unique() :", x.unique())   # x.unique() : [42 52 36 24 73]

print("df['age'].unique() : ",  df['age'].unique())     # df['age'].unique() :  [42 52 36 24 73]

print("----------------------------------")
# Transposing your data:
df_t = df.T
print("df_t = df.T:\n", df_t)

# Sorting by an axis: ejes

print("----------------------------------")
df_sort = df.sort_index(axis=0, ascending=True)
print("filas -> 0 - df.sort_index(axis=1, ascending=False):\n", df_sort)

print("----------------------------------")
df_sort = df.sort_index(axis=1, ascending=False)
print("columnas -> 1 - df.sort_index(axis=1, ascending=False):\n", df_sort)

print("----------------------------------")
print("ordena por nombre de columna - df.sort_values(by='fname'):\n", df.sort_values(by='fname'))

print("----------------------------------")

# Dot Notation
print("filas 0,1 - df[0:2]:", df[0:2])
print("filas 1,2,3 - df[1:4]: ", df[1:4])

print("una posición especifica df: lname[4] - df['lname'][4]:\n", df['lname'][4])  # Cooze
print("una posición especifica df: lname[4] - df.lname[4]:\n", df.lname[4])  # Cooze
print("df.lname[0]:\n", df.lname[0])        #   Miller
print("----------------------------------")
#
"""
loc_pandas.py
se basa en las etiquetas; 
cuando se utilizan dos argumentos se usan los encabezados de las columnas y 
el índice de filas para seleccionar los datos que se desean, 
también pude tomar un número entero como número de fila o de columna.
"""
print("Access the column using the name - df.loc[0, 'lname']: ",  df.loc[0, 'lname'])   # df.loc[0,'lname']:  Miller
print("Access posición 1 de la columna lname - df.loc[1, 'lname']: ",  df.loc[1, 'lname'])   # df.loc[1,'lname']:  Jacobson

print("Access multiples columns using their names, - tres columnas de la fila - df.loc[1,['lname','age', 'value' ]]:\n", df.loc[1, ['lname', 'age', 'value']])

"""
lname    Jacobson
age            52
value        94.0
Name: 1, dtype: object
"""
print("La fila 3 del df - df.loc[[3]]:\n", df.loc[[3]])
print("La fila 3 del df - df.loc[df.index[3]]:\n", df.loc[df.index[3]])

print("Todas las filas de las columnas - df.loc[:, ['fname', 'age']]:\n", df.loc[:, ['fname', 'age']])

print("la posición 2 de la columna:\n", df.loc[df.index[2], 'age'])

print("Imprime el df completo - df.loc[df.index]:\n", df.loc[df.index])

print("Slicing the dataframe using name - df.loc[0:2, 'fname':'age']:\n", df.loc[0:2, 'fname':'age'])

print("fila 3, columna fname - df.at[3, 'fname']: ", df.at[3, 'fname'])     # Jake
# print("fila 3, columna fname - df.at[3, 'fname']: ", df.at[[3], ['fname']])     # TypeError: unhashable type: 'list'

# select column by Label - DataFrame -
X = df.loc[df.index[0:3], ['fname']]
print("X = df.loc[df.index[0:3], ['fname']]:\n", X)

print("----------------------------------------------")
"""
iloc_pandas.py
basado en números enteros.
Utiliza números de columna y números de fila para obtener los
datos en posiciones particulares en el df
"""
print("1st row and the 1st column - df.iloc[[0],[0]]:\n", df.iloc[[0], [0]])  # 0
print("1st row and the 1st column - df.iloc[0, 0]:\n", df.iloc[0, 0]) # 0

print("2nd row and the 1st column - df.iloc[2, 1]:\n", df.iloc[2, 1]) # Tina

print("fila 0 y columna2 - df.iloc[0, 2]:\n", df.iloc[0, 2]) # Miller

print("fila1 y columnas 0, 1, y 2 - df.iloc[1, [0, 1, 2]]:\n", df.iloc[1, [0, 1, 2]])
"""
number           1
fname        Molly
lname     Jacobson
Name: 1, dtype: object
"""
print("fila 3, columna 0 - df.at[3, 0]: ", df.iat[3, 0])     # 3
# print("fila 3, columna 0 - df.at[[3], [0]]: ", df.iat[[3], [0]])     # ValueError: iAt based indexing can only have integer indexers

X = df.iloc[df.index[0:2], [3]]
print("X = df.iloc[df.index[0:2], [3]]:\n", X)
"""
X = df.iloc[df.index[0:2], [3]]:
    age
0   42
1   52
"""
print("----------------------------------------------")
df_gt_30 = df['age'] >= 30
print("Comparaciones - df_gt_30=df['age'] >= 30:\n", df_gt_30)
"""
0     True
1     True
2     True
3    False
4     True
Name: age, dtype: bool
"""
print("---------------dot.notation-------------------")
df_age_ge30 = df.age >= 30
print("df.age >= 30:\n", df_age_ge30, "type: ", type(df_age_ge30))
""" 
0     True
1     True
2     True
3    False
4     True

Name: age, dtype: bool type:  <class 'pandas.core.series.Series'>
"""

print("----------------------------------------------")
df_iloc = df.iloc[0:3, 0:4]
print("slicing fila de 0 a 3 y columnas de 0 a 4 -df_iloc = df.iloc[0:3, 0:4]:\n", df_iloc)

"""
    number  fname     lname  age
0       0  Jason    Miller   42
1       1  Molly  Jacobson   52
2       2   Tina         .   36
"""
print("----------------------------------------------")
# Get multiple columns as a dataframe - Crea un dataframe de varias columna del dframe
y = (df[['age', 'value', 'purchase']])

print("Get multiple columns as a dataframe - df[['age', 'value', 'purchase']]:\n", y)
print("type(y)", type(y))           # pandas.core.frame.DataFrame
print("dir (y) :", dir(y))

print("----------------------------------------------")

print("columna 'value', position 2 - df['value'][2]:\n", df['value'][2])     #  57.0

print("-------------------dot notation---------------------------")
print("devuelve bool (T, F) si cumple la condición - df.age.isin([42 , 52]):\n", df.age.isin([42 , 52]))
"""
df.age.isin([42 , 52]):
 0     True
1     True
2    False
3    False
4    False
Name: age, dtype: bool
"""


# comprobar el tipo de datos del DataFrame
print(datosDF.dtypes)

print(datosDF["normalized-losses"])

# obtener un resumen estadistico del DataFrame
print(datosDF.describe(include="all"))

# obtener estadiscas por columnas del DataFrame
print(datosDF[["length", "compression-ratio"]].describe())

# informacion del DataFrame con Pandas

print(datosDF.info)
