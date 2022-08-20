"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        stack = [root]
        res = []
        
        while stack:
            cur = stack.pop()
            if cur != None:
                
                res.append(cur.val)

                if cur.children:
                    for i in range(len(cur.children)-1,-1,-1):
                        stack.append(cur.children[i])
                
        return res
            
        
        