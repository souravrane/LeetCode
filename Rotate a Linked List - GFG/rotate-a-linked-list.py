# Your task is to complete this function

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''


class Solution:
    
    def reverse(self, head):
        prev = None
        cur = head
        
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        return prev
        
    def size(self, head):
        count = 0
        cur = head
        
        while cur:
            count += 1
            cur = cur.next
        
        return count
        
    #Function to rotate a linked list.
    def rotate(self, head, k):
        
        length = self.size(head)
        
        if k == length: return head
        
        h1 = self.reverse(head)
        i = 1
        cur = h1
        while i < length - k:
            i += 1
            cur = cur.next
        
        h2 = cur.next
        cur.next = None
    
        h1 = self.reverse(h1)
        
            
        h2 = self.reverse(h2)
        
        cur = h1
        while cur.next:
            cur = cur.next
        
        cur.next = h2
        return h1
        
        
#{ 
#  Driver Code Starts
# driver

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self,val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

def printList(n):
    while n:
        print(n.data, end=' ')
        n = n.next
    print()

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]
        k = int(input())
        
        lis = LinkedList()
        for i in arr:
            lis.insert(i)
        
        head = Solution().rotate(lis.head,k)
        printList(head)
# } Driver Code Ends