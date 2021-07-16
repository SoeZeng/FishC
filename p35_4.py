# -*- coding: utf-8 -*-
"""
Created on Wed May 12 19:32:13 2021

@author: ZYS
"""

import easygui as g
import os

code_statistics = {'.py':[0,0]}

def code_docum(file_path):
    print(file_path)
    os.chdir(file_path)
    for each_file in os.listdir(os.curdir):
       
       key = os.path.splitext(each_file)[1]
       if key in code_statistics.keys():
          
           with open(each_file,encoding='UTF-8') as f:
               line = 0
               try: 
                   for each in f:
                       line += 1
               except UnicodeDecodeError:
                   pass # 不可避免会遇到格式不兼容的文件，这里忽略掉......
               #print(line) 
               code_statistics[key][0] += 1
               code_statistics[key][1] += line
               
       elif os.path.isdir(each_file):     
           code_docum(each_file)
           os.chdir(os.pardir)
        

file_path = g.diropenbox('请选择您的代码库','浏览文件夹')
code_docum(file_path)

total_line = 0
text = ''
for key,value in code_statistics.items():
    total_line += value[1]
    text = text + ('【%s】源文件%d个，源代码%d行\n' % (key,value[0],value[1]))
msg = '您目前共累计编码了%d行代码，完成进度：%.2f%%\n离十万行代码还差%d行，请继续努力！' % (total_line,total_line/1000,100000-total_line)
title = '统计结果'
g.textbox(msg,title,text)


'''
import easygui as g
import os

def show_result(start_dir):
    lines = 0
    total = 0
    text = ""

    for i in source_list:
        lines = source_list[i]
        total += lines
        text += "【%s】源文件 %d 个，源代码 %d 行\n" % (i, file_list[i], lines)
    title = '统计结果'
    msg = '您目前共累积编写了 %d 行代码，完成进度：%.2f %%\n离 10 万行代码还差 %d 行，请继续努力！' % (total, total/1000, 100000-total)
    g.textbox(msg, title, text)

def calc_code(file_name):
    lines = 0
    with open(file_name) as f:
        print('正在分析文件：%s ...' % file_name)
        try:
            for each_line in f:
                lines += 1
        except UnicodeDecodeError:
            pass # 不可避免会遇到格式不兼容的文件，这里忽略掉......
    return lines

def search_file(start_dir) :
    os.chdir(start_dir)
    
    for each_file in os.listdir(os.curdir) :
        ext = os.path.splitext(each_file)[1]
        if ext in target :
            lines = calc_code(each_file) # 统计行数
            # 还记得异常的用法吗？如果字典中不存，抛出 KeyError，则添加字典键
            # 统计文件数
            try:
                file_list[ext] += 1
            except KeyError:
                file_list[ext] = 1
            # 统计源代码行数
            try:
                source_list[ext] += lines
            except KeyError:
                source_list[ext] = lines
            
        if os.path.isdir(each_file) :
            search_file(each_file) # 递归调用
            os.chdir(os.pardir) # 递归调用后切记返回上一层目录
            
target = ['.c', '.cpp', '.py', '.cc', '.java', '.pas', '.asm']
file_list = {}
source_list = {}

g.msgbox("请打开您存放所有代码的文件夹......", "统计代码量")
path = g.diropenbox("请选择您的代码库：")

search_file(path)
show_result(path)
'''

