"""


HackerRank
30 day Coding Challenge
Day 9:
Factorials
@author Kynan Bertulli

"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    num = n
    f = 1
    if (num > 1):
        return num * (factorial(num-1))
    else:
        num = 1
        return num
    return(num)

if __name__ == '__main__':

    n = int(input())

    result = factorial(n)

    print(result)