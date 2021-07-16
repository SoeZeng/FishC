# -*- coding: utf-8 -*-
"""
Created on Mon May 24 12:10:20 2021

@author: DELL
"""

class CountList:
    def __init__(self,*args):
        self.values = [x for x in args]
        self.count = {}.fromkeys(range(len(self.values)),0)
        self.length = len(self.values)

    def __len__(self):
        return self.length    
    
    def __getitem__(self,key):      # key为下标索引
        self.count[key] += 1         
        return self.values[key] 
    
    def __delitem__(self,key):
        self.values.pop(key)
        self.count.pop(key)
    
    def __reversed__(self):
        self.values.reverse()
        for i in range(self.length//2):
            self.count[i],self.count[self.length-i] = self.count[self.length-i],self.count[i] 
    
    def append(self,value):
        self.values.append(value)
        self.count[self.length] = 0
        self.length += 1
    
    def pop(self,key):
        self.values.pop(key)
        for i in range(key,self.length-1):
            self.count[i] = self.count[i+1]
        self.length -= 1
        self.count.pop(self.length)
        
    
    def remove(self,value):
        index = self.values.index(value)
        self.values.remove(value)
        for i in range(index,self.length-1):
            self.count[i] = self.count[i+1]
        self.length -= 1
        self.count.pop(self.length)
    
    def insert(self,key,value):
        self.values.insert(key, value)
        for i in range(key,self.length):
            self.count[key+1] = self.count[key]
        self.count[key] = value
        self.length += 1
    
    def clear(self):
        self.values.clear()
        self.count.clear()
        self.length = 0
        

'''
class CountList(list):
    def __init__(self, *args):
        super().__init__(args)
        self.count = []
        for i in args:
            self.count.append(0)

    def __len__(self):
        return len(self.count)

    def __getitem__(self, key):
        self.count[key] += 1
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        self.count[key] += 1
        super().__setitem__(key, value)

    def __delitem__(self, key):
        del self.count[key]
        super().__delitem__(key)

    def counter(self, key):
        return self.count[key]

    def append(self, value):
        self.count.append(0)
        super().append(value)

    def pop(self, key=-1):
        del self.count[key]
        return super().pop(key)

    def remove(self, value):
        key = super().index(value)
        del self.count[key]
        super().remove(value)

    def insert(self, key, value):
        self.count.insert(key, 0)
        super().insert(key, value)

    def clear(self):
        self.count.clear()
        super().clear()

    def reverse(self):
        self.count.reverse()
        super().reverse()

'''
    
    