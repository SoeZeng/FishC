# -*- coding: utf-8 -*-
"""
Created on Sun May 23 21:11:05 2021

@author: DELL
"""

import pickle
import os

class Record:
    def __init__(self,attr):
        self.file_name = '%s.pkl' % attr
        self.value = None
        
    def __get__(self,instance,owner):
        return self.value
    
    def __set__(self,instance,value):
        self.value = value
        with open(self.file_name,'wb') as p:
            pickle.dump(self.value,p)
            
    def __delete__(self,instance):
        del instance
        os.remove(self.file_name)
            
class Test:
    x = Record('x')
    y = Record('y')


'''
import os
import pickle

class MyDes:
    saved = []

    def __init__(self, name = None):
        self.name = name
        self.filename = self.name + '.pkl'

    def __get__(self, instance, owner):
        if self.name not in MyDes.saved:
            raise AttributeError("%s 属性还没有赋值！" % self.name)

        with open(self.filename, 'rb') as f:
            value = pickle.load(f)

        return value

    def __set__(self, instance, value):
        with open(self.filename, 'wb') as f:
            pickle.dump(value, f)
            MyDes.saved.append(self.name)

    def __delete__(self, instance):
        os.remove(self.filename)
        MyDes.saved.remove(self.name)

'''