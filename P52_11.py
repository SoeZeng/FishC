# -*- coding: utf-8 -*-
"""
Created on Thu May 27 20:24:28 2021

@author: DELL
"""

dict1 = {}
dict1[1] = 1
dict1['1'] = 2
dict1[1.0] = 3   #覆盖dict1[1]

result = 0
for each in dict1:
    #print(dict1[each])
    result += dict1[each]

print(result)