# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 12:09:08 2019

@author: antonio.furnari
"""
def is_leap(year):
    leap = False
    
    # Write your logic here
    
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False

year = int(raw_input())
print is_leap(year)