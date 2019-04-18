"""

HackerRank
30 day Coding Challenge
Day 11:
2D Array
@author Kynan Bertulli

input
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

output:
7

"""
#!/bin/python3

import math
import os
import random
import re
import sys




if __name__ == '__main__':
    arr = []
    res = 0
    newarr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            # print(arr[i][j])
            if(j + 2 <  len(arr[i]) and i + 2 <  len(arr)):
                res = (int(arr[i][j]) + int(arr[i][j+1]) + int(arr[i][j+2])
                          + int(arr[i+1][j+1])
                          + int(arr[i+2][j]) + int(arr[i+2][j+1]) + int(arr[i+2][j+2]))
            newarr.append(res)

    print(max(newarr))