# -*- coding: utf-8 -*-
"""
Created on Thu May 27 10:28:35 2021

@author: DELL
"""
'''
class Const:
    def __inti__(self):
        self.attrs = []
        
    def __setattr__(self,name,value):
        if self.attrs.index(name):
            if (name.isupper()):
                self.attrs.append(name)
                self.__dict__[name] = value
            else:
                raise TypeError('常量名必须由大写字母组成！')
        else:
            raise TypeError('常量名无法改变！')
 '''           


# 该模块用于让 Python 支持常量操作
class Const:    
    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise TypeError('常量无法改变！')
            
        if not name.isupper():
            raise TypeError('常量名必须由大写字母组成！')

        self.__dict__[name] = value

import sys
sys.modules[__name__] = Const()
        

           
        
        