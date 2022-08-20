"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def helper(self, root):
        if root == None: return
        self.result.append(root.val)

        if root.children:
            for node in root.children:
                self.helper(node)

    
    def preorder(self, root: 'Node') -> List[int]:
        self.result = []
        self.helper(root)
        return self.result
        
        