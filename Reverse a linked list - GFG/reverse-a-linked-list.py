#function Template for python3
import sys
sys.setrecursionlimit(10000000)
"""
# Node Class

class node:
    def __init__(self, val):
        self.data = val
        self.next = None

# """    
# 1
# <-1<-2
class Solution:
    def __init__(self):
        self.newHead = None
        
    def reverseLL(self, head):
        if head.next == None:
            self.newHead = head
            return head
        
        tail = self.reverseLL(head.next)
        tail.next = head
        tail = tail.next
        tail.next = None
        return tail
    
    #Function to reverse a linked list.
    def reverseList(self, head):
        self.reverseLL(head)
        return self.newHead
        



#{ 
#  Driver Code Starts
# Node Class    
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

def printList(head):
    tmp = head
    while tmp:
        print(tmp.data, end=' ')
        tmp=tmp.next
    print()

if __name__=='__main__':
    for i in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]
        
        lis = Linked_List()
        for i in arr:
            lis.insert(i)
        
        newHead = Solution().reverseList(lis.head)
        printList(newHead)

# } Driver Code Ends