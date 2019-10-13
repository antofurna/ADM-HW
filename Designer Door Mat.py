# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 11:52:05 2019

@author: antonio.furnari
"""

N, M = map(int,input().split()) #9, 27
for i in range(1,N,2):
    print ((".|."*i).center(M, "-"))
print (("WELCOME").center(M, "-"))
for i in range(N-2,-1,-2):
    print ((".|."*i).center(M, "-"))# Enter your code here. Read input from STDIN. Print output to STDOUT