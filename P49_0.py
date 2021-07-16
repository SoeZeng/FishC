# -*- coding: utf-8 -*-
"""
Created on Tue May 25 21:23:30 2021

@author: DELL
"""

def myRev(string):
    index = len(string)
    while index > 0:
        yield string[index-1]
        index -= 1
    
for i in myRev('FishC'):
    print(i,end='')

    

'''
def myRev(data):
    # 这里用 range 生成 data 的倒序索引
    # 注意，range 的结束位置是不包含的
    for index in range(len(data)-1, -1, -1):
        yield data[index]'''