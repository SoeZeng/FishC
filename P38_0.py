# -*- coding: utf-8 -*-
"""
Created on Sat May 15 20:22:33 2021

@author: DELL
"""

import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    
class Line:
    def __init__(self, p1, p2):
        self.x = p1.x - p2.x
        self.y = p1.y - p2.y
        
    def getLen(self):
        Len = math.sqrt(self.x ** 2 + self.y ** 2)
        return Len
    
p1 = Point(1,1)
p2 = Point(4,5)
line = Line(p1,p2)
print(line.getLen())

'''
import math

class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

class Line():
    def __init__(self, p1, p2):
        self.x = p1.getX() - p2.getX()
        self.y = p1.getY() - p2.getY()
        self.len = math.sqrt(self.x*self.x + self.y*self.y)

    def getLen(self):
        return self.len

>>> p1 = Point(1, 1)
>>> p2 = Point(4, 5)
>>> line = Line(p1, p2)
>>> line.getLen()
5.0

'''