# -*- coding: utf-8 -*-
"""
Created on Fri May 14 21:16:36 2021

@author: DELL
"""
'''
import random as r

legal_x = [0,10]
legal_y = [0,10]

class Turtle:
    def __init__(self):
        self.num = 1
        self.step = [1,2]
        self.energy = 100
        self.position_x = r.randint(legal_x[0], legal_x[1])
        self.position_y = r.randint(legal_y[0], legal_y[1])
        self.position = (self.position_x,self.position_y)
    
    def move(self):
        move_step = r.choice(self.step)
        self.position = move_position(Turtle, self.position_x, self.position_y,move_step)
        self.energy -= move_step

class Fish:
    def __init__(self):
        self.num = 10
        self.step = 1
        self.positions = []
        for i in range(self.num):
            self.position_x = r.randint(legal_x[0], legal_x[1])
            self.position_y = r.randint(legal_y[0], legal_y[1])
            self.position = (self.position_x,self.position_y)
            self.positions.append(self.position)
            
    def move(self):
        for i in range(self.num):
            self.positions[i] = move_position(Fish, self.positions[i][0], self.positions[i][1],self.step)
            
        
def move_position(player,position_x,position_y,move_step):
    move_directions = r.choice(['L','R','U','D'])
    
    move_position_x = [position_x - move_step,position_x + move_step]
    move_position_y = [position_y - move_step,position_y + move_step]
    if move_directions == 'L':
        position_x = move_position_x[0] if move_position_x[0] >= legal_x[0] else move_position_x[1]
    elif move_directions == 'R':    
        position_x = move_position_x[1] if move_position_x[1] <= legal_x[1] else move_position_x[0]
    elif move_directions == 'D':
        position_y = move_position_y[0] if move_position_y[0] >= legal_y[0] else move_position_y[1]
    else:   
        position_y = move_position_y[1] if move_position_y[1] <= legal_y[1] else move_position_y[0]
    return  position_x,position_y   

t = Turtle()
f = Fish()
while t.energy > 0 and f.num > 0:
    cnt = 0
    while cnt < f.num:
        if t.position == f.positions[cnt]:
            f.positions.pop(cnt)
            print('有一条鱼被吃掉啦！')
            f.num -= 1
            t.energy += 20
        else:
            cnt += 1
            
    t.move()
    f.move()


print('乌龟的体力都耗尽啦，游戏结束！') if t.energy <= 0 else print('鱼儿都被吃掉啦，游戏结束！')
'''
    


import random as r

legal_x = [0, 10]
legal_y = [0, 10]

class Turtle:
    def __init__(self):
        # 初始体力
        self.power = 100
        # 初始位置随机
        self.x = r.randint(legal_x[0], legal_x[1])
        self.y = r.randint(legal_y[0], legal_y[1])

    def move(self):
        # 随机计算方向并移动到新的位置（x, y）
        new_x = self.x + r.choice([1, 2, -1, -2])
        new_y = self.y + r.choice([1, 2, -1, -2])
        # 检查移动后是否超出场景x轴边界
        if new_x < legal_x[0]:
            self.x = legal_x[0] - (new_x - legal_x[0])
        elif new_x > legal_x[1]:
            self.x = legal_x[1] - (new_x - legal_x[1])
        else:
            self.x = new_x
        # 检查移动后是否超出场景y轴边界
        if new_y < legal_y[0]:
            self.y = legal_y[0] - (new_y - legal_y[0])
        elif new_y > legal_y[1]:
            self.y = legal_y[1] - (new_y - legal_y[1])
        else:
            self.y = new_y        
        # 体力消耗
        self.power -= 1
        # 返回移动后的新位置
        return (self.x, self.y)

    def eat(self):
        self.power += 20
        if self.power > 100:
            self.power = 100

class Fish:
    def __init__(self):
        self.x = r.randint(legal_x[0], legal_x[1])
        self.y = r.randint(legal_y[0], legal_y[1])
        
    def move(self):
        # 随机计算方向并移动到新的位置（x, y）
        new_x = self.x + r.choice([1, -1])
        new_y = self.y + r.choice([1, -1])
        # 检查移动后是否超出场景x轴边界
        if new_x < legal_x[0]:
            self.x = legal_x[0] - (new_x - legal_x[0])
        elif new_x > legal_x[1]:
            self.x = legal_x[1] - (new_x - legal_x[1])
        else:
            self.x = new_x
        # 检查移动后是否超出场景y轴边界
        if new_y < legal_y[0]:
            self.y = legal_y[0] - (new_y - legal_y[0])
        elif new_y > legal_y[1]:
            self.y = legal_y[1] - (new_y - legal_y[1])
        else:
            self.y = new_y
        # 返回移动后的新位置
        return (self.x, self.y)

turtle = Turtle()
fish = []
for i in range(10):
    new_fish = Fish()
    fish.append(new_fish)

while True:
    if not len(fish):
        print("鱼儿都吃完了，游戏结束！")
        break
    if not turtle.power:
        print("乌龟体力耗尽，挂掉了！")
        break

    pos = turtle.move()
    # 在迭代器中删除列表元素是非常危险的，经常会出现意想不到的问题，因为迭代器是直接引用列表的数据进行引用
    # 这里我们把列表拷贝给迭代器，然后对原列表进行删除操作就不会有问题了^_^
    for each_fish in fish[:]:
        if each_fish.move() == pos:
            # 鱼儿被吃掉了
            turtle.eat()
            fish.remove(each_fish)
            print("有一条鱼儿被吃掉了...")


        
        
        
        