# -*- coding: utf-8 -*-
"""
Created on Sun May  9 09:57:44 2021

@author: DELL
"""

import easygui as g
import random


secret = random.randint(1,10)
msg = '不妨猜一下小甲鱼现在心里想的是哪个数字：'
title = '数字小游戏'
guess = g.integerbox(msg,title,lowerbound=1,upperbound=10)

while True:
    if guess == secret:
        g.msgbox("你是小甲鱼心里的蛔虫吗？！",title)
        g.msgbox("哼，猜中了也没有奖励！",title)
        break
    else:
        if guess > secret:
            g.msgbox("哥，大了大了~~~",title)
        else:
            g.msgbox("嘿，小了，小了~~~",title)
        guess = g.integerbox(msg,title,lowerbound=1,upperbound=10)
        
g.msgbox("游戏结束，不玩啦^_^")


'''
import random
import easygui as g

g.msgbox("嗨，欢迎进入第一个界面小游戏^_^")
secret = random.randint(1,10)

msg = "不妨猜一下小甲鱼现在心里想的是哪个数字（1~10）："
title = "数字小游戏"
guess = g.integerbox(msg, title, lowerbound=1, upperbound=10)

while True:
    if guess == secret:
        g.msgbox("我草，你是小甲鱼心里的蛔虫吗？！")
        g.msgbox("哼，猜中了也没有奖励！")
        break
    else:
        if guess > secret:
            g.msgbox("哥，大了大了~~~")
        else:
            g.msgbox("嘿，小了，小了~~~")   
        guess = g.integerbox(msg, title, lowerbound=1, upperbound=10)
            
g.msgbox("游戏结束，不玩啦^_^")
'''