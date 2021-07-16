# -*- coding: utf-8 -*-
"""
Created on Sun May  9 10:50:59 2021

@author: DELL
"""

import easygui as g

msg = '【*真实姓名】为必填项\n【*手机号码】为必填项\n【*E-mail】为必填项'
title = '账号中心'
fields = ['*用户名','*真实姓名','固定电话','*手机号码','QQ','*E-mail']

while 1:
    values = g.multenterbox(msg,title,fields)
    errmsg = ''
    for i in range(len(fields)):
        if fields[i][0] == '*' and values[i].strip() == '':
            errmsg = ('%s为必填项，请重新输入！' % fields[i])
            g.msgbox(errmsg,title)
            break
    if errmsg == '':
        break
    
    
'''
import easygui as g

msg = "请填写以下联系方式"
title = "账号中心"
fieldNames = [" *用户名", " *真实姓名", "  固定电话", " *手机号码", "  QQ", " *E-mail"]
fieldValues = []
fieldValues = g.multenterbox(msg, title, fieldNames)

while 1:
    if fieldValues == None:
        break
    errmsg = ""
    for i in range(len(fieldNames)):
        option = fieldNames[i].strip()
        if fieldValues[i].strip() == "" and option[0] == "*":
            errmsg += ('【%s】为必填项。\n\n' % fieldNames[i])
    if errmsg == "":
        break
    fieldValues = g.multenterbox(errmsg, title, fieldNames, fieldValues)

print("用户资料如下：%s" % str(fieldValues))
    
'''