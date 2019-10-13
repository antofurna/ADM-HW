# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 12:07:46 2019

@author: antonio.furnari
"""

if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())

X = [[i,j,k] for i in range(x + 1) for j in range(y + 1) for k in range (z+1) if (i + j + k) != n]
print  (X)
