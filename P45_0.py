# -*- coding: utf-8 -*-
"""
Created on Sun May 23 15:47:28 2021

@author: DELL
"""

class C:
    def __getattr__(self, name):
        return '属性不存在！'
    
c = C()
print(c.x)