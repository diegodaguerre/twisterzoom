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

def getValue(raw_line):
	
	print "RAW LINE: " + raw_line
	
	return values