# -*- coding: utf-8 -*-
"""
Created on Sun May  9 21:04:55 2021

@author: DELL
"""

import easygui as g
import os

file_path = g.fileopenbox()

file = open(file_path)
file_name = os.path.basename(file_path)
msg = '文件【%s】的内容如下：' % file_name
title = '显示文件内容'
#file = open(file_path)
text = file.read()
g.textbox(msg,title,text)
file.close()



'''
import easygui as g
import os

file_path = g.fileopenbox(default="*.txt")

with open(file_path) as f:
    title = os.path.basename(file_path)
    msg = "文件【%s】的内容如下：" % title
    text = f.read()
    g.textbox(msg, title, text)
'''