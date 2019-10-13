# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 12:11:23 2019

@author: antonio.furnari
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())

if ( 1>=a or a >= 10**10 ) or ( 1>=b or b >=10**10 ) :
    print("Number too large or too small");
else:
    c= a+b
    print (c);
    d=a-b
    print(d);
    e=a*b
    print(e);
