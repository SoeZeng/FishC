# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 19:33:30 2021

@author: DELL
"""

import os

file_types = {}
path = os.getcwd()
#(file_name,file_extension) = os.path.splitext(path)
file_list = os.listdir(path)
#print(file_list)
for file in file_list:
    key = os.path.splitext(file)[1]
    key = '文件夹' if key == '' else key
    if key not in file_types:
        file_types[key] = 1
    else:
        file_types[key] += 1
for key,value in file_types.items():
    print("该文件夹下共有类型为【%s】的文件%d个" % (key,value))
    
'''
import os

all_files = os.listdir(os.curdir) # 使用os.curdir表示当前目录更标准
type_dict = dict()

for each_file in all_files:
    if os.path.isdir(each_file):
        type_dict.setdefault('文件夹', 0)
        type_dict['文件夹'] += 1
    else:
        ext = os.path.splitext(each_file)[1]
        type_dict.setdefault(ext, 0)
        type_dict[ext] += 1

for each_type in type_dict.keys():
    print('该文件夹下共有类型为【%s】的文件 %d 个' % (each_type, type_dict[each_type]))

'''