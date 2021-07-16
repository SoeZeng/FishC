# -*- coding: utf-8 -*-
"""
Created on Tue May 25 15:49:40 2021

@author: DELL
"""

class MyRev:
    def __init__(self,string):
        self.str = list(string)
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.str:
            char = self.str.pop(-1)
            return char
        else:
            raise StopIteration
            
myRev = MyRev('FishC')
for i in myRev:
    print(i,end='')
    
    
'''
class MyRev:
    def __init__(self, data):
        self.data = data
        self.index = len(data)
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == 0:
            raise StopIteration

        self.index = self.index - 1
        return self.data[self.index]
'''