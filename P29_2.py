# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 21:10:46 2021

@author: DELL
"""

def Print(FileName,N):
    f = open(FileName)
    count = 0
    for line in f:
        count += 1
        if count < N:
            print(line,end='')
        else:
            break
    f.close()
        
file_name = input("请输入要打开的文件：")
n = int(input("请输入需要显示该文件前几行："))
Print(file_name,n)