# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 11:56:30 2019

@author: antonio.furnari
"""

def count_substring(string, sub_string):
    conta= 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            conta +=1
    return conta   
        

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)