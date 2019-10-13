### 1 - Say Hello with python
"""
Created on Sun Oct 13 12:13:58 2019

@author: antonio.furnari
"""


if __name__ == '__main__':
    print "Hello, World!"
	

### 2 - Python If-Else
"""
Created on Sun Oct 13 12:12:29 2019

@author: antonio.furnari
"""

#!/bin/python

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(raw_input().strip())

    if (n % 2 == 0):
        if (2 <= n <= 5):
            print("Not Weird");
        if (6 <= n <= 20):
            print("Weird");
        if (n > 20):
            print("Not Weird")
    else:
        print("Weird")

### 3 - Arithmetic Operators

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

### 4 - Python_Division
"""
Created on Sun Oct 13 12:10:45 2019

@author: antonio.furnari
"""

from __future__ import division

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())

    c= a//b
    print (c);
    d=a/b
    print(d);

### 5 - Loops
"""
Created on Sun Oct 13 12:10:00 2019

@author: antonio.furnari
"""

if __name__ == '__main__':
    n = int(raw_input())

if 1<= n <= 20 :
    for i in range (0,n):
        print(i**2)
else:
    print("Error, number too large or too small")
### 6 - Write a Function
"""
Created on Sun Oct 13 12:09:08 2019

@author: antonio.furnari
"""
def is_leap(year):
    leap = False
    
    # Write your logic here
    
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False

year = int(raw_input())
print is_leap(year)
### 7 - Print Function
"""
Created on Sun Oct 13 12:08:46 2019

@author: antonio.furnari
"""

from __future__ import print_function

if __name__ == '__main__':
    n = int(raw_input())

for i in range(1, n+1):
    print (i, end='')
### 8 - List Comprehensions
"""
Created on Sun Oct 13 12:07:46 2019

@author: antonio.furnari
"""

if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())

X = [[i,j,k] for i in range(x + 1) for j in range(y + 1) for k in range (z+1) if (i + j + k) != n]
print  (X)
### 9 - Find the Runner-Up Score!
"""
Created on Sun Oct 13 12:06:39 2019

@author: antonio.furnari
"""

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())

print(sorted(list(set(arr)))[-2])
### 10 - Finding the percentage
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
### 11 - Lists
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
### 12 - Tuples
"""
Created on Sun Oct 13 12:02:52 2019

@author: antonio.furnari
"""

if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())

tupla = tuple(integer_list)
print hash(tupla)
### 13 - sWAP cASE
"""
Created on Sun Oct 13 12:02:30 2019

@author: antonio.furnari
"""

def swap_case(s):
    L = s.swapcase()
    return L
    
   # print(L)


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

### 14 - String Split and Join
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

### 15 - What's Your Name
"""
Created on Sun Oct 13 12:00:21 2019

@author: antonio.furnari
"""

def print_full_name(a, b):
    print("Hello %s %s! You just delved into python." % (a, b))
    
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
### 16 - Mutations
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
### 17 - Find a string
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
### 18 - String Validators
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

### 19 - Text Alignment
"""
Created on Sun Oct 13 11:48:47 2019

@author: antonio.furnari
"""

#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

### 20 - Text Wrap
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
### 21 - Designer Door Mat
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

### 22 - Capitalize!
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 08:36:38 2019

@author: antonio.furnari
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    return ' '.join([word.capitalize() for word in s.split(' ')]) 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()





