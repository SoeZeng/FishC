# -*- coding: utf-8 -*-
"""
Created on Wed May 19 12:14:07 2021

@author: DELL
"""

class Nstr(str):
    def __init__(self,s):
        self.asc = 0
        for c in s:
            self.asc += ord(c)
    
    def __add__(self,other):
        return int(self.asc) + int(other.asc)
            
    
    def __sub__(self,other):
        return int(self.asc) - int(other.asc)
    
    def __mul__(self,other):
        return int(self.asc) * int(other.asc)
    
    def __truediv__(self,other):
        return int(self.asc) / int(other.asc)
    
    def __floordiv__(self,other):
        return int(self.asc) // int(other.asc)
    
a = Nstr('FishC')
b = Nstr('love')
print(a+b)
print(a-b)
print(a/b)
print(a//b)
print(a*b)

'''
class Nstr:
    def __init__(self, arg=''):
        if isinstance(arg, str):
            self.total = 0
            for each in arg:
                self.total += ord(each)
        else:
            print("参数错误！")

    def __add__(self, other):
        return self.total + other.total

    def __sub__(self, other):
        return self.total - other.total

    def __mul__(self, other):
        return self.total * other.total

    def __truediv__(self, other):
        return self.total / other.total

    def __floordiv__(self, other):
        return self.total // other.total

'''

'''
class Nstr(int):
    def __new__(cls, arg=0):
        if isinstance(arg, str):
            total = 0
            for each in arg:
                total += ord(each)
            arg = total
        return int.__new__(cls, arg)

'''