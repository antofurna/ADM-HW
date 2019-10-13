# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 12:05:03 2019

@author: antonio.furnari
"""

if __name__ == '__main__':
    n = int(raw_input())
    voti = {}
    for i in range(n):
        a = raw_input().split(' ')
        voti[a[0]] = [float(x) for x in a[1:]]
    studente = raw_input()
    print "%.2f" %(sum(voti[studente])/len(voti[studente]))