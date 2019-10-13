# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 11:53:46 2019

@author: antonio.furnari
"""

import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)