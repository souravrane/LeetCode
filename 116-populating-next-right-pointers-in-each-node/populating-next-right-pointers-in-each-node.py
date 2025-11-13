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
        if not root: return root
        cur = root
        nxt = root.left

        while cur and nxt:

            while cur:
                if cur.left: cur.left.next = cur.right
                if cur.next and cur.right:
                    cur.right.next = cur.next.left
                cur = cur.next
            
            cur = nxt
            nxt = nxt.left
        return root