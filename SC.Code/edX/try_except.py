#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 19:08:27 2020
IN-WORK-OUT
@author: scelis
"""

# =============================================================================
# try / except Structure => Control de errores => No va a saltar un Traceback 
# 
# Si el código del try funciona => No se ejecuta le exception
# Si el código del try NO funciona => Se ejecuta la exception
# =============================================================================
    
astr = 'Hello Bob'
#sabemos que esto puede fallar ó no
try:
    istr = int(astr)
except:
    istr = -1
print('First', istr)

astr = '123'
#sabemos que esto puede fallar ó no
try:
    istr = int(astr)
except:
    istr = -1    
print('Second', istr)

print('All done')
print('==========')   

rawstr = input('Escriba un número: ')
try:
    ival = int(rawstr)
except:
    ival = -1

if ival > 0:
    print ('Has escrito: ', ival)
else:
    print ('No es un número')

print('All done')
print('==========')     
