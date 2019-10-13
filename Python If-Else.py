# -*- coding: utf-8 -*-
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