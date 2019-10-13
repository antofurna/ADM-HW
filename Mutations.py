# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 11:59:37 2019

@author: antonio.furnari
"""

def mutate_string(string, position, character):
  #return
  #  string = "abracadabra"
    l = list(string)
    l[position] = character
    string = ''.join(l)
    return string
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)