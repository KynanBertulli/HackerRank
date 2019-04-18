"""
3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry

HackerRank
30 day Coding Challenge
Day 8:
Dictionaries

@author Kynan Bertulli

"""


if __name__ == '__main__':
    dict1 ={}
    for i in range(int(input())):
        d1 = input().split(" ")
        dict1.update({d1[0]: d1[1]})

    while True:
        inp = input()
        if inp == "":
            break
        if(dict1.get(inp)):
            print(inp + "="+dict1[inp])
        elif(dict1.get(inp) == None):
            print("Not found")


