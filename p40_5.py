# -*- coding: utf-8 -*-
"""
Created on Tue May 18 12:02:01 2021

@author: DELL
"""

class CodeA:
    @staticmethod
    def foo():
        print("调用静态方法 foo()")




'''
import time
 
def timeslong(func):
    def call():
        start = time.process_time()
        print("It's time starting ! ")
        func()
        print("It's time ending ! ")
        end = time.process_time()
        return "It's used : %s ." % (end - start)
    return call

@timeslong
def f():
    y = 0
    for i in range(10):
        y = y + i + 1
        print(y)
    return y

print(f())

'''
