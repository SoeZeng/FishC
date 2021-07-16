# -*- coding: utf-8 -*-
"""
Created on Tue May 18 16:26:50 2021

@author: DELL
"""

'''

class C2F:
    def __init__(self,C):
        self.F = C * 1.8 + 32
        self.getF()
    
    def getF(self):
        return self.F
    
print(C2F(32))

'''

class C2F(float):
        "摄氏度转换为华氏度"
        def __new__(cls, arg=0.0):
                return float.__new__(cls, arg * 1.8 + 32)

print(C2F(32))