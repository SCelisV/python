#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 19:08:27 2020
IN-WORK-OUT
@author: scelis
"""

# =============================================================================
# try / except Structure
# 
# if the code in the try work => the exception is skipped:
# if the code in the try fails => it salta a la except section5:
# =============================================================================
    
astr = 'Hello Bob'
istr = int(astr)
print('First', istr)
astr = '123'
istr = int(astr)
print('Second', istr)
print('All Done')
print('==========')