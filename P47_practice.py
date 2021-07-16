# -*- coding: utf-8 -*-
"""
Created on Mon May 24 10:25:16 2021
'
@author: DE'"LL
"""

'''
class Nlist:
    def __init__(self):
        self.count = []
        for i in range(len(self)):
            self.count[i] == 0
        
    def __getitem__(self,key):
        if key != 'count':
            self.count[key] += 0 
        return self.key
    '''
    
    
class CountList:
    def __init__(self,*args):
        self.values = [x for x in args]
        self.count = {}.fromkeys(range(len(self.values)),0)

    def __len__(self):
        return len(self.values)    
    
    def __getitem__(self,key):      # key为下标索引
        self.count[key] += 1         
        return self.values[key] 
    