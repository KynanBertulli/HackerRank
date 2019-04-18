"""

HackerRank
30 day Coding Challenge
Day 9:
Binary Numbers
@author Kynan Bertulli

"""

#!/bin/python3

import math
import os
import random
import re
import sys


# 65535
if __name__ == '__main__':
    n = int(input())
    ls = []
    while(round(n) > 0):
        i = n % 2
        ls.append(int(i))
        n = n / 2
    ls.reverse()
    c =0
    count = []
    for i in range(len(ls)):
        if(ls[i] == 1):
            c += 1
            # print(str(ls[i]) + "" + str(i))
        elif (ls[i] == 0):
            c = 0
        count.append(c)

    print(c)
    print(ls)
    print(count)
    print(max(count))
    #  must use enhanced for loop for list of ints
    # res = ''.join(str(e) for e in ls)
    # print(res)