# -*- coding: utf-8 -*-
"""
Created on Wed May 19 10:46:34 2021

@author: DELL
"""

class Nstr(str):
    def __sub__(self,other):
        result = self
        while True:            
            index = result.find(other)
            if index == -1:
                break
            else:
                l = len(other)    
                result = result[:index] + result[index+l:]
        return result
    
a = Nstr('MJQiiiiiii')
b = Nstr('i')
print(a-b)




'''
class Nstr(str):
    def __sub__(self, other):
        return self.replace(other, '')


a = Nstr('MJQiiiiiii')
b = Nstr('i')
print(a-b)
'''