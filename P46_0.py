# -*- coding: utf-8 -*-
"""
Created on Sun May 23 20:23:06 2021

@author: DELL
"""

class MyDes:
    def __init__(self,value,key):
        self.value = value
        self.key = key
    
    def __get__(self,instance,owner):
        print('正在获取变量：', self.key)
        return self.value
    
    def __set__(self,instance,value):
        print('正在修改变量：', self.key)
        self.value = value
    
    def __delete__(self,instance):
        print('噢~这个变量没法删除~')

class Test:
    x = MyDes(10,'x')
    

'''
class MyDes:
    def __init__(self, initval=None, name=None):
        self.val = initval
        self.name = name

    def __get__(self, instance, owner):
        print("正在获取变量：", self.name)
        return self.val

    def __set__(self, instance, value):
        print("正在修改变量：", self.name)
        self.val = value

    def __delete__(self, instance):
        print("正在删除变量：", self.name)
        print("噢~这个变量没法删除~")

'''