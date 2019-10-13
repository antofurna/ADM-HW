# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 12:02:30 2019

@author: antonio.furnari
"""

def swap_case(s):
    L = s.swapcase()
    return L
    
   # print(L)


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)