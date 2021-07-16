# -*- coding: utf-8 -*-
"""
Created on Tue May 18 10:54:33 2021

@author: DELL
"""

class A:
    count = 0
    def __init__(self):
        A.count += 1
       
    def __del__(self):
        A.count -= 1
        
a = A()
b = A()
c = A()
del b
del c
print(A.count)
    