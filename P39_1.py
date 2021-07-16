# -*- coding: utf-8 -*-
"""
Created on Tue May 18 11:12:14 2021

@author: DELL
"""

class Stack:
    def __init__(self):
        self.stack = []
    
    def isEmpty(self):
        print(True) if len(self.stack) == 0 else print(False)
            
    def push(self,data):
        self.stack.append(data)

    
    def pop(self):
        self.stack.remove(self.stack[-1])

    
    def top(self):
        print(self.stack[-1])
    
    def buttom(self):
        print(self.stack[0])
        
s = Stack()
s.isEmpty()
s.push(666)
s.push(888)
s.isEmpty()
s.top()
s.buttom()
s.pop()
s.isEmpty()


'''
class Stack:
    def __init__(self, start=[]):
        self.stack = []
        for x in start:
            self.push(x)

    def isEmpty(self):
        return not self.stack
    
    def push(self, obj):
        self.stack.append(obj)
 
    def pop(self):
        if not self.stack:
            print('警告：栈为空！')
        else:
            return self.stack.pop()
 
    def top(self):
        if not self.stack:
            print('警告：栈为空！')
        else:
            return self.stack[-1]
 
    def bottom(self):
        if not self.stack:
            print('警告：栈为空！')
        else:
            return self.stack[0]
'''