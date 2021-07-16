# -*- coding: utf-8 -*-
"""
Created on Tue May 18 14:43:04 2021

@author: DELL
"""

class C:
    def __init__(self, size=10):
        self.size = size

    @property
    def XSize(self):
        return self.size

    @XSize.setter
    def XSize(self, value):
        self.size = value

    @XSize.deleter
    def XSize(self):
        del self.size

    
c = C()
print(c.size)
c.size = 12
print(c.size)
del c.size