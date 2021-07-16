# -*- coding: utf-8 -*-
"""
Created on Fri May 21 11:21:43 2021

@author: DELL
"""

import time as t

class Mytimer:
    def __init__(self,func,number=1000000):
        self.prompt = '未开始计时！'
        self.lasted = 0.0
        self.begin = 0
        self.end = 0
        self.default_timer = t.perf_counter
        self.func =func
        self.number = number
    
    
    def __str__(self):
        return self.prompt
    
    __repr__ = __str__
    
    def __add__(self,other):
        prompt = '总共运行了 %.2f 秒' % (self.lasted + other.lasted)
        return prompt
    
   
    def timing(self):
        self.begin = self.default_timer()
        for i in range(self.number):
            self.func()
        self.end = self.default_timer()
        self.lasted = self.end - self.begin
        self.prompt = '总共运行了 %.2f 秒' % (self.lasted)
        
    def set_time(self,timer):
        if timer == 'process_time':
            self.default_timer = t.process_time
        elif timer == 'perf_counter':
            self.default_timer = t.perf_counter
        else:
            print("输入无效，请输入 perf_counter 或 process_time")
            
def test():
    text = "I love FishC.com!"
    char = 'o'
    if char in text:
        pass
    
t1 = Mytimer(test)
t1.timing()
print(t1)