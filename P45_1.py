# -*- coding: utf-8 -*-
"""
Created on Sun May 23 17:01:18 2021

@author: DELL
"""

class Demo:
    def __getattr__(self, name):
        self.name = 'FishC'
        return self.name
    