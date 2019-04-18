"""

HackerRank
30 day Coding Challenge
Day 15:
LinkedList
@author Kynan Bertulli


"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:

    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def __init__(self):
        self.head = None

    def insert(self,head,data):
        NewNode = Node(data)
        print(str(NewNode.data))
        if self.head is None:
            self.head = NewNode
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next=NewNode
        return self.head
    #Complete this method

mylist= Solution()
T=int(input())
head = None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
    # print("Head: ", head)
mylist.display(head);
