# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 12:01:27 2019

@author: antonio.furnari
"""

def split_and_join(line):
    # write your code here
    line = line.split(" ")
    line  = "-".join(line)
    return line
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)