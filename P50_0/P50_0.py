# -*- coding: utf-8 -*-
"""
Created on Thu May 27 11:18:04 2021

@author: DELL
"""

import const


const.NAME = 'MJQ'
print(const.NAME)

try:
    const.NAME = 'DCX'
except TypeError as Err:
    print(Err)
 
try:
    const.name = 'MJQ'
except TypeError as Err:
    print(Err)
