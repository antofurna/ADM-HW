# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 12:10:00 2019

@author: antonio.furnari
"""

if __name__ == '__main__':
    n = int(raw_input())

if 1<= n <= 20 :
    for i in range (0,n):
        print(i**2)
else:
    print("Error, number too large or too small")