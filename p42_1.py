# -*- coding: utf-8 -*-
"""
Created on Wed May 19 11:35:45 2021

@author: DELL
"""

class Nstr(str):
    def __lshift__(self,other):
        return self[other:] + self[:other]  
    
    def __rshift__(self,other):
        return self[-other:] + self[:-other]
 
a = Nstr('I Love FishC.com!')    
print(a<<3)
print(a>>3)