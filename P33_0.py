# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 20:38:59 2021

@author: DELL
"""

import random

def guess_exam(temp,secret):
    try:
        guess = eval(temp)
        while guess != secret:
            guess = eval(input("哎呀，猜错了，请重新输入吧："))
            if guess == secret:
                print("我草，你是小甲鱼心里的蛔虫吗？！")
                print("哼，猜中了也没有奖励！")
            else:
                if guess > secret:
                    print("哥，大了大了~~~")     
                else:
                    print("嘿，小了，小了~~~")
        print("游戏结束，不玩啦^_^")
    except:
        guess = input("输入有误！请重新输入一个数字：")
        guess_exam(guess,secret)

secret = random.randint(1,10)
print('------------------我爱鱼C工作室------------------')
temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
guess_exam(temp,secret)

'''
import random

secret = random.randint(1,10)
print('------------------我爱鱼C工作室------------------')
temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
try:    
    guess = int(temp)
except ValueError:
    print('输入错误！')
    guess = secret
while guess != secret:
    temp = input("哎呀，猜错了，请重新输入吧：")
    guess = int(temp)
    if guess == secret:
        print("我草，你是小甲鱼心里的蛔虫吗？！")
        print("哼，猜中了也没有奖励！")
    else:
        if guess > secret:
            print("哥，大了大了~~~")
        else:
            print("嘿，小了，小了~~~")
print("游戏结束，不玩啦^_^")

'''

