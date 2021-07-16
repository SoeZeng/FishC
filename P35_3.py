# -*- coding: utf-8 -*-
"""
Created on Sun May  9 21:24:36 2021

@author: DELL
"""

import easygui as g
import os

file_path = g.fileopenbox(default="*.txt")

with open(file_path) as f:
    title = os.path.basename(file_path)
    msg = "文件【%s】的内容如下：" % title
    text = f.read()
    text_updated = g.textbox(msg, title, text)
if text != text_updated:
    msg1 = '检测到内容发生改变，请选择以下操作：'
    title1 = '警告'
    buttons1 = ['覆盖保存','放弃操作','另存为...']
    choice = g.buttonbox(msg1,title1,buttons1)
    if choice == '覆盖保存':
        with open(file_path,'r+') as f0:
            f0.write(text_updated)
    elif choice == '另存为...':
        file1_path = g.filesavebox(default='.txt')
        with open(file1_path,'w') as f1:
            f1.write(text_updated)
        
'''
import easygui as g
import os

file_path = g.fileopenbox(default="*.txt")

with open(file_path) as old_file:
    title = os.path.basename(file_path)
    msg = "文件【%s】的内容如下：" % title
    text = old_file.read()
    text_after = g.textbox(msg, title, text)
    
if text != text_after[:-1]:
    # textbox 的返回值会追加一个换行符
    choice = g.buttonbox("检测到文件内容发生改变，请选择以下操作：", "警告", ("覆盖保存", "放弃保存", "另存为..."))
    if choice == "覆盖保存":
        with open(file_path, "w") as old_file:
            old_file.write(text_after[:-1])
    if choice == "放弃保存":
        pass
    if choice == "另存为...":
        another_path = g.filesavebox(default=".txt")
        if os.path.splitext(another_path)[1] != '.txt':
            another_path += '.txt'
        with open(another_path, "w") as new_file:
            new_file.write(text_after[:-1])

'''