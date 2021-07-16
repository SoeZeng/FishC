# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 20:50:44 2021

@author: DELL
"""

import os

def search_save(start_dir) :
    os.chdir(start_dir)
    
    for each_file in os.listdir(os.curdir) :
        file_ext = os.path.splitext(each_file)[1]
        if file_ext == '.txt' :
            path.append(os.getcwd() + os.sep + each_file + os.linesep) # 使用os.sep是程序更标准
        if os.path.isdir(each_file) :
            search_save(each_file) # 递归调用
            os.chdir(os.pardir) # 递归调用后切记返回上一层目录

start_dir = input('请输入待查找的初始目录：')
path = []
search_save(start_dir)
f = open("path.txt",'w')
f.writelines(path)
f.close()