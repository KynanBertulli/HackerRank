""""
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
"""


# in future:
# UPDATE with switch statement
if __name__ == '__main__':
    # N = int(input())
    a1 =[]
    result = []
    for i in range(int(input())):
        a1.append(input())
    print(a1)
    for i in range(len(a1)):
        a2 = a1[i].split()
        name = a2[0]
        if(name == "insert"):
            result.insert(int(a2[1]), int(a2[2]))
        elif(name == "print"):
            print(str(result))
        elif(name == "remove"):
            result.remove(int(a2[1]))

        elif (name == "reverse"):
            result.reverse()

        elif(name == "append"):
            result.append(int(a2[1]))

        elif(name == "sort"):
            result.sort()

        elif (name == "pop"):
            result.pop()
