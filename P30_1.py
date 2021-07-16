# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 20:06:30 2021

@author: DELL
"""

import os

file_list = os.listdir(os.curdir)
for file in file_list:
    if os.path.isfile(file):
        print("%s【%dBytes】" % (file,os.path.getsize(file)))