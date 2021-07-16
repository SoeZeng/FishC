# -*- coding: utf-8 -*-
"""
Created on Fri May 14 11:01:54 2021

@author: DELL
"""

class Rectangle:
    length = 5.00
    width = 4.00
    
    def setRect(self):
        print('请输入矩形的长和宽：')
        self.length = eval(input('长：'))
        self.width = eval(input('宽：'))
        
    def getRect(self):
        print('这个矩形的长是%.2f，宽是%.2f' % (self.length,self.width))
        
    def getArea(self):
        print(self.length * self.width)
        
rect = Rectangle()
rect.getRect()
rect.setRect()
rect.getArea()