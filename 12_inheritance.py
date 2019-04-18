"""

HackerRank
30 day Coding Challenge
Day 12:
Inheritance
@author Kynan Bertulli

input
Heraldo Memelli 8135627
2
100 80

output:
Name: Memelli, Heraldo
ID: 8135627
Grade: O


"""


class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


# inherit from person
class Student(Person):
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.

    def __init__(self, firstName, lastName, id, scores):
        Person.__init__(self, firstName, lastName, id)
        self.scores = scores

    def calculate(self):
        arr = self.scores
        res = sum(arr) / len(arr)
        ans = ""
        if( res >= 90 and res <= 100):
            ans = "O"
            return ans
        elif(res >= 80 and res <= 90):
            ans = "E"
            return ans
        elif(res >= 70 and res <= 80):
            ans = "A"
            return ans
        elif(res >= 55 and res <= 70):
            ans = "P"
            return ans
        elif(res >= 40 and res <= 55):
            ans = "D"
            return ans
        elif(res < 40):
            ans = "T"
            return ans

    #   Function Name: calculate
    #   Return: A character denoting the grade.


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())