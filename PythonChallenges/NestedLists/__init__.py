"""

HackerRank
Nested Lists



@author Kynan Bertulli


N -
"""

if __name__ == '__main__':
    namelist = []
    scorelist = []
    classlist = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        namelist.append(name)
        scorelist.append(score)
    classlist.append([namelist, scorelist])

    dict1 = dict(zip(namelist, scorelist))
    sortedlist = sorted(scorelist)
    students = [x[0] for x in classlist if x[0] == scorelist[1]]
    students.sort()

    for a in range(len(students)):
        print(students[a])

    # output:
    # print(namelist)
    # print(scorelist)
    # print(sortedlist)
    # print(classlist)
    # print(dict1)
