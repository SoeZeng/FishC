# -*- coding: utf-8 -*-
"""
Created on Tue May 25 12:58:27 2021

@author: DELL
"""
'''
alist = range(5)
it = iter(alist)

while True:
    try:
        print(next(it))
    except StopIteration:
        break

'''
class fo:
    def __init__(self,n=5):
        self.cnt = -1
        self.n = n
        
    def __iter__(self):
        return self
    
    def __next__(self):
        self.cnt += 1
        if self.cnt < self.n:  
            return self.cnt     
        else:
            raise StopIteration

f = fo()
while True:
    try:
        print(next(f))
    except StopIteration:
        break
