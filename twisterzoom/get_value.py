#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Esta función se encarga de convertir información que envía la estación
metereogica en una linea a un diccionario.

De esto:
WIND 	   6.5	  277

A esto:
['WIND',6.5,277]

"""
import re


def getValue(raw_line):
    print "RAW LINE: " + raw_line
    #return values

if __name__ == "__main__":
    a = "algo"
    getValue(a)
  
  
"""
example: 
from get_value import getValue
getValue("WIND 6.34 234")
RAW LINE: WIND 6.34 234
"""