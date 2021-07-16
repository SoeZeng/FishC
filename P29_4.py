# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 16:33:25 2021

@author: DELL
"""

def replace(file_name,str1,str2):
    f_read = open(file_name)
    count = 0
    content = []
    for line in f_read:
        if str1 in line:
            #count += 1
            count += line.count(str1)
            line = line.replace(str1, str2)
        content.append(line)
    f_read.close()
    option = input("文件%s中共有%d个【%s】\n您确定要把所有【%s】替换成【%s】吗\n【YES/NO】:" % (file_name,count,str1,str1,str2))
    if option in ['YES','yes','Yes']:
        f_write = open(file_name,'w')
        f_write.writelines(content)
        f_write.close()
    
file_name = input("请输入文件名：")
str1 = input("请输入要替换的单词或字符：")
str2 = input("请输入新的单词或字符：")
replace(file_name,str1,str2)