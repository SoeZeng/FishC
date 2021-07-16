# -*- coding: utf-8 -*-
"""
Created on Tue May 25 13:58:26 2021

@author: DELL
"""

class LeapYear:
    def __init__(self):
        self.year = 2021
        
    def __iter__(self):
        return self
    
    def __next__(self):
        while not ((self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)):
            self.year -= 1  
        year = self.year
        self.year -= 1
        return year
        
            
leapYears = LeapYear()
for i in leapYears:     # 循环一次执行一次__next__(),将返回值赋值给i，再对i进行判断，决定是否执行下一次循环
                        # 若类外没有设置判断条件，需要在类内设置，不满足条件则抛出StopIteration异常，退出for循环
    if i >= 2000:
        print(i)
    else:
        break
    
'''
import datetime as dt

class LeapYear:
    def __init__(self):
        self.now = dt.date.today().year

    def isLeapYear(self, year):
        if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
            return True
        else:
            return False
        
    def __iter__(self):
        return self

    def __next__(self):
        while not self.isLeapYear(self.now):
            self.now -= 1 

        temp = self.now
        self.now -= 1
        
        return temp
'''
        