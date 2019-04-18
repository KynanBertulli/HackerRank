"""

HackerRank
30 day Coding Challenge
Day 16:
exceptions
@author Kynan Bertulli


"""
#!/bin/python3

import sys


S = input().strip()

try:
    i = int (S)
    print(i)
except ValueError:
    print ('Bad String')
