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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        cur = root
        while cur and cur.left:
            level = cur
            while level:
                level.left.next = level.right
                if level.next:
                    level.right.next = level.next.left
                level = level.next
            cur = cur.left
            
        return root