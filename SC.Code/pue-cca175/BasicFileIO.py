#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
* Use the built-in ﬁle object and its methods
– Methods: open(), read(), readline(), and close()
– File modes: r=read, w=write, a=append
– File format: b=binary, t=text (default)

@author: ¯\_(ツ)_/¯

"""

line =' '
file = open('files/loudacre.log','rt')
while True:
    line = file.readline()
    record = line.split(',')
    if not line:
        break
    print(record)
file.close()
