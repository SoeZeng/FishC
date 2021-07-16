# -*- coding: utf-8 -*-
"""
Created on Tue May 18 11:58:18 2021

@author: DELL
"""

class C:
    def __init__(self, size=10):
        self.size = size

    def getXSize(self):
        return self.size

    def setXSize(self, value):
        self.size = value

    def delXSize(self):
        del self.size

    x = property(getXSize,setXSize,delXSize)
    
c = C()
print(c.x)
c.x = 12
print(c.x)
del c.x

