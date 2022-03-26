#how floating point numbers will behave on your system

# >>> import sys
# >>> sys.float_info   
# esto es lo que muestra mi ubuntu:
sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)

###

64 bits para representar flotantes 
2 ** 64 == 18,446,744,073,709,551,616

para valores como max=1.7976931348623157e+308, y epsilon=2.220446049250313e-16
no hay suficiente espacio, así que se aproximan al número representable más cercano. 

>>> 0.3 - 0.1 * 3 # this should be 0!!!
-5.551115123125783e-17



###
