# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 02:43:39 2021

@author: Frostmoon
"""

def rgb(r, g, b):
    if (r > 255):
        r = 255
   
    if (r < 0):
       r = 0
   
    if (g > 255):
        g = 255
        
    if (g < 0):
        g = 0     
        
    if (b > 255):
        b = 255
        
    if (b < 0):
        b = 0
        
    r = hex(r)[2:].zfill(2).upper()
    g = hex(g)[2:].zfill(2).upper()
    b = hex(b)[2:].zfill(2).upper()
        
    return r + g + b
    
print(rgb(-20, 275, 125))
