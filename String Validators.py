# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 11:55:24 2019

@author: antonio.furnari
"""

if __name__ == '__main__':
    s = input()

s1 = any([i.isalnum() for i in s])
s2 = any([i.isalpha() for i in s])
s3 = any([i.isdigit() for i in s])
s4 = any([i.islower() for i in s])
s5 = any([i.isupper() for i in s])
print(s1)
print(s2)
print(s3)
print(s4)
print(s5)