# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 12:06:39 2019

@author: antonio.furnari
"""

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())

print(sorted(list(set(arr)))[-2])