"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        cur = root

        while cur:
            dummy = Node(0)
            temp = dummy

            while cur:
                if cur.left:
                    temp.next = cur.left
                    temp = temp.next
                
                if cur.right:
                    temp.next = cur.right
                    temp = temp.next
                
                cur = cur.next
            
            cur = dummy.next
        
        return root