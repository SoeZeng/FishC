# -*- coding: utf-8 -*-
"""
Created on Fri May 14 21:16:33 2021

@author: DELL
"""

class Ticket_Price:
        
    def compute_price(self,adult_num = 0,child_num = 0,isWeekend = False):
        self.price = 120  if isWeekend else 100
        self.total_price = (adult_num  + child_num * 0.5) * self.price
        
        return self.total_price
    
tp = Ticket_Price()
print('两个小孩一个成人平日票价为：%.2f' % tp.compute_price(2,1))


'''
class Ticket():
        def __init__(self, weekend=False, child=False):
                self.exp = 100
                if weekend:
                        self.inc = 1.2
                else:
                        self.inc = 1
                if child:
                        self.discount = 0.5
                else:
                        self.discount = 1
        def calcPrice(self, num):
                return self.exp * self.inc * self.discount * num

>>> adult = Ticket()
>>> child = Ticket(child=True)
>>> print("2个成人 + 1个小孩平日票价为：%.2f" % (adult.calcPrice(2) + child.calcPrice(1)))
2个成人 + 1个小孩平日票价为：250.00

'''