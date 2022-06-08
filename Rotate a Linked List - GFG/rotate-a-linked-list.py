# Your task is to complete this function

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''


class Solution:
    
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
        rotations = k % length
        if rotations == 0: return head
        
        # circular ll
        cur = head
        while cur.next:
            cur = cur.next
        cur.next = head
        
        cur = head
        x = 0
        while x < rotations - 1:
            x += 1
            cur = cur.next
        
        h1 = cur.next
        cur.next = None
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