# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 14:16:55 2021

@author: DELL
"""

def int_input(ipt):
    while True:
        try:
            int(input(ipt))
            break
        except ValueError:
            print("出错，您输入的不是一个整数！")

int_input('请输入一个整数：')