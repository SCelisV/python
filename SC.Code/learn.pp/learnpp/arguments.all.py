#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
transcript: SCelis

# arguments.all.py
Al definir una función, 
- los positional arguments van primero ( name ), 
- luego cualquier default arguments ( name=value ), 
- luego los Variable positional arguments, ( *name or simply * )
- luego cualquier keyword-only arguments, (cualquier name or name=value form )
y luego cualquier variable keyword arguments ( **name )

Por otro lado, cuando se llama a una función, los argumentos deben darse en el siguiente orden:
- positional arguments first ( value ), 
- luego cualquier combinación de keyword arguments ( name=value ), variable positional arguments ( *name ), 
y luego variable keyword arguments ( **name ).

"""
# arguments.all.py

def func(a, b, c=7, *args, **kwargs):
    print('a, b, c:', a, b, c)                          
    print('args:', args)                                
    print('kwargs:', kwargs)                            

func(1, 2, 3, *(5, 7, 9), **{'A': 'a', 'B': 'b'})   #  usando unpacking operators para iterables y dictionaries
"""
a, b, c: 1 2 3
args: (5, 7, 9)
kwargs: {'A': 'a', 'B': 'b'}}
"""
func(1, 2, 3, 5, 7, 9, A='a', B='b')                # usando sintaxis explicita 
"""
a, b, c: 1 2 3
args: (5, 7, 9)
kwargs: {'A': 'a', 'B': 'b'}
"""