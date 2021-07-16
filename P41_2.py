# -*- coding: utf-8 -*-
"""
Created on Tue May 18 16:47:38 2021

@author: DELL
"""

class Nint(int):
    def __new__(cls,pref):
        
        if isinstance(pref,str):   
            result = 0
            for c in pref[:]:
                result += ord(c)
            pref = result
        return int.__new__(cls,pref)
        '''    
        elif isinstance(pref,float):
            print('浮点型数据')
            result = pref // 1
            
        else:
            print('整型数据')
            result = pref
            
        return int.__new__(cls,result)
        '''
        
print(Nint(123))
print(Nint(1.5))
print(Nint('A'))
print(Nint('FishC'))

'''
class Nint(int):
        def __new__(cls, arg=0):
                if isinstance(arg, str):
                        total = 0
                        for each in arg:
                                total += ord(each)
                        arg = total
                return int.__new__(cls, arg)

'''
            