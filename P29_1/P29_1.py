# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 20:27:32 2021

@author: DELL
"""

def FileCompare(FileName1,FileName2):
    f1 = open(FileName1)
    f2 = open(FileName2)
    count = 0                #统计行数
    differ = []
    for line1 in f1:
        line2 = f2.readline()
        count += 1
        if line1 != line2:
            differ.append(count)
    f1.close()
    f2.close()
    return differ

file_name1 = input("请输入一个文件名：")
file_name2 = input("请输入另一个文件名：")
differ = FileCompare(file_name1, file_name2)
if len(differ) == 0:
    print("两个文件完全相同!")
else:
    print("两个文件有【%d】处不同：" % len(differ))
    for each in differ:
        print("第%d行不同" % each)
    
        
                