# -*- coding: utf-8 -*-
"""
Created on Tue May 18 15:22:03 2021

@author: DELL
"""

class FileObject:
    def __init__(self,file_name = 'poet.txt'):
        self.f = open(file_name)
        print('文件已打开！')
    
    def __del__(self):
        self.f.close()
        print('文件已关闭！')
        
        
f = FileObject()
del f
