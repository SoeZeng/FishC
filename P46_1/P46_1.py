# -*- coding: utf-8 -*-
"""
Created on Sun May 23 20:35:53 2021

@author: DELL
"""

import time as t

class Record:
    def __init__(self,value,key):
        self.value = value
        self.key = key
        
    def __get__(self,instance,owner):
        read_time = t.asctime()
        with open('record.txt','a') as f:
            f.write('%s 变量于北京时间 %s 被读取，%s = ' % (self.key,read_time,self.key) + str(self.value) + '\n')
        return self.value
    
    def __set__(self,instance,value):
        self.value = value
        update_time = t.asctime()
        with open('record.txt','a') as f:
            f.write('%s 变量于北京时间 %s 被修改，%s = ' % (self.key,update_time,self.key) + str(self.value) + '\n')
            
class Test:
    x = Record(10,'x')
    y = Record(8.8, 'y')
    

'''
import time

class Record:
    def __init__(self, initval=None, name=None):
        self.val = initval
        self.name = name
        self.filename = "record.txt"

    def __get__(self, instance, owner):
        with open(self.filename, 'a', encoding='utf-8') as f:
            f.write("%s 变量于北京时间 %s 被读取，%s = %s\n" % \
                    (self.name, time.ctime(), self.name, str(self.val)))
        return self.val

    def __set__(self, instance, value):
        filename = "%s_record.txt" % self.name
        with open(self.filename, 'a', encoding='utf-8') as f:
            f.write("%s 变量于北京时间 %s 被修改, %s = %s\n" % \
                    (self.name, time.ctime(), self.name, str(value)))
        self.val = value
        
'''