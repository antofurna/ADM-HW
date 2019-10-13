# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 12:04:14 2019

@author: antonio.furnari
"""

if __name__ == '__main__':
    N = int(raw_input())

lista = []
for _ in range(N):
    s = raw_input().split()
    comando = s[0]
    argomento = s[1:]
    if comando !="print":
        comando += "("+ ",".join(argomento) +")"
        eval("lista."+comando)
    else:
        print lista
