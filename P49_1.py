# -*- coding: utf-8 -*-
"""
Created on Tue May 25 21:31:36 2021

@author: DELL

"""
'''
import math

def is_prime(num):
    if num > 1:
        
        if num == 2:
            return True
        
        if num % 2 == 0:
            return False
        
        for i in range(3,int(math.sqrt(num)) + 1,2):
            if num % i == 0:
                return False
        
        return True
    
    return False

Sum = 0
for i in range(2000000):
    if is_prime(i):
        Sum += i 
        
print(Sum)
''' 


import math

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False

def get_primes(number):
    while True:
        if is_prime(number):
            yield number
        number += 1

def solve():
    total = 2
    for next_prime in get_primes(3):
        if next_prime < 2000000:
            total += next_prime
        else:
            print(total)
            return

if __name__ == '__main__':
    solve()   