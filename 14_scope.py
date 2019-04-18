"""

HackerRank
30 day Coding Challenge
Day 14:
Scope
@author Kynan Bertulli

• A class constructor that takes
an array of integers as a parameter and saves it to the Elements instance variable.

A computeDifference method that
finds the maximum absolute difference between any 2 numbers in N
and stores it in the maximumDifference instance variable.

"""
class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here

    def computeDifference(self):
        ls = self.__elements
        ls2 = []
        for i,j in ls2:
            print(ls2)
    def maximumDifference(a):
        print(1)

# End of Difference class



_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)