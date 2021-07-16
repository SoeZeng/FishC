# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 20:01:55 2021

@author: DELL
"""

import pickle

def save_file(boy,girl):
    boy_txt = open("boy_%d.txt" % count,'wb')
    pickle.dump(boy,boy_txt)
    boy_txt.close()
    
    '''
    boy_txt = open("boy_%d.txt" % count,'rb')
    print(pickle.load(boy_txt))
    boy_txt.close()
    '''
    girl_txt = open("girl_%d.txt" % count,'wb')
    pickle.dump(girl,girl_txt)
    girl_txt.close()
    boy.clear()
    girl.clear()

f = open("record.txt")
count = 1
boy = []
girl = []
for line in f:
    if line[:6] != '======':
        line_split = line.split(':',1)
        if line_split[0] == '小甲鱼':
            boy.append(line_split[1])
        else:
            girl.append(line_split[1])
    else:
        save_file(boy,girl)
        count += 1
save_file(boy,girl)
f.close()

'''
import pickle

def save_file(boy, girl, count):
    file_name_boy = 'boy_' + str(count) + '.txt'
    file_name_girl = 'girl_' + str(count) + '.txt'

    boy_file = open(file_name_boy, 'wb') # 记得一定要加 b 吖
    girl_file = open(file_name_girl, 'wb') # 记得一定要加 b 吖

    pickle.dump(boy, boy_file)
    pickle.dump(girl, girl_file)

    boy_file.close()
    girl_file.close()

def split_file(file_name):
    count = 1
    boy = []
    girl = []

    f = open(file_name)

    for each_line in f:
        if each_line[:6] != '======':
            (role, line_spoken) = each_line.split(':', 1)
            if role == '小甲鱼':
                boy.append(line_spoken)
            if role == '小客服':
                girl.append(line_spoken)
        else:
            save_file(boy, girl, count)

            boy = []
            girl = []
            count += 1 

    save_file(boy, girl, count)
    f.close()

split_file('record.txt')

'''