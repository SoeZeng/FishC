# -*- coding: utf-8 -*-
"""
Created on Wed May 19 15:22:18 2021

@author: DELL
"""
'''
class C:
    def __init__(self,*args):
        self.len = len(args)
        print('并没有传入参数') if self.len == 0 else print('传入了 %d 个参数，分别是：' % self.len,args)
        
c = C()
c = C(1,2,3)
'''


class C:
        def __init__(self, *args):
                if not args:
                        print("并没有传入参数")
                else:
                        print("传入了 %d 个参数，分别是：" % len(args), end='')
                        for each in args:
                                print(each, end=' ')
