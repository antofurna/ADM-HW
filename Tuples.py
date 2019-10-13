# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 12:02:52 2019

@author: antonio.furnari
"""

if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())

tupla = tuple(integer_list)
print hash(tupla)
