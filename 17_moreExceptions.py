"""

HackerRank
30 day Coding Challenge
Day 17:
More Exceptions
@author Kynan Bertulli

4
3 5
2 4
-1 -2
-1 3

10
10 0
0 10
-1 4
2 -3
-2 -2
5 6
3 3
8 0
2 3
3 -3
"""
class Calculator:
    def power(self, n,p):
        try:

            if (n < 0 or p<0):
                raise ValueError
            else:
                return n**p
        except ValueError:
            return "n and p should be non-negative"


#Write your code here
print()

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:

        ans=myCalculator.power(n,p)

        print(ans)
    except Exception as e:
        print(e)