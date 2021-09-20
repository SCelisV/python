#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
transcript: SCelis

# arguments.all.kwonly.py
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
# arguments.all.kwonly.py

def func_with_kwonly(a, b=42, *args, c, d=256, **kwargs):           # los keyword-only son:  c, d=256 después de *args variable positional
                                                                    # sería igual si vinieran después de un * (con lo que no hay arg positional variable)
    print('a, b:', a, b)
    print('c, d:', c, d)
    print('args:', args)
    print('kwargs:', kwargs)

func_with_kwonly(3, 42, c=0, d=1, *(7, 9, 11), e='E', f='F')
"""
a, b: 3 42
c, d: 0 1
args: (7, 9, 11)
kwargs: {'e': 'E', 'f': 'F'}
"""
func_with_kwonly(3, 42, *(7, 9, 11), c=0, d=1, e='E', f='F')
"""
a, b: 3 42
c, d: 0 1
args: (7, 9, 11)
kwargs: {'e': 'E', 'f': 'F'}
"""