#User function Template for python3

''' structure of list node:

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

'''
from collections import defaultdict
class Solution:
    def findIntersection(self, head1, head2):
        # code here
        # return head of intersection list
        h = defaultdict(int)
        
        cur = head2
        while cur:
            h[cur.data] += 1
            cur = cur.next
        
        dummy = Node(-1)
        tail = dummy
        
        cur = head1
        while cur:
            if cur.data in h:
                tail.next = Node(cur.data)
                tail = tail.next
                h[cur.data] -= 1
                
            cur = cur.next
        
        return dummy.next
#{ 
#  Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def insert(self,data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

def printList(head):
    while head:
        print(head.data,end=' ')
        head=head.next

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        
        n1 = int(input())
        arr1 = [int(x) for x in input().split()]
        ll1 = linkedList()
        for i in arr1:
            ll1.insert(i)
        
        n2 = int(input())
        arr2 = [int(x) for x in input().split()]
        ll2 = linkedList()
        for i in arr2:
            ll2.insert(i)
        
        result = Solution().findIntersection(ll1.head,ll2.head)
        printList(result)
        print()

# } Driver Code Ends