# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 20:18:37 2021

@author: DELL
"""

import os

def search_file(root_path,file_name):
    file_list = os.listdir(root_path)
    #print(root_path)
    for file in file_list:
        if file == file_name:
            file_path.append(root_path+'\\'+file_name)
        elif os.path.isdir(file):
            search_file(root_path+'\\'+file, file_name)
    
            
file_path = []
root_path = input("请输入待查找的初始目录：")
file_name = input("请输入需要查找的目标文件：")
search_file(root_path, file_name)
for each in file_path:
    print(each)
    
'''
import os

def search_file(start_dir, target) :
    os.chdir(start_dir)
    
    for each_file in os.listdir(os.curdir) :
        if each_file == target :
            print(os.getcwd() + os.sep + each_file) # 使用os.sep是程序更标准
        if os.path.isdir(each_file) :
            search_file(each_file, target) # 递归调用
            os.chdir(os.pardir) # 递归调用后切记返回上一层目录

start_dir = input('请输入待查找的初始目录：')
target = input('请输入需要查找的目标文件：')
search_file(start_dir, target)

'''