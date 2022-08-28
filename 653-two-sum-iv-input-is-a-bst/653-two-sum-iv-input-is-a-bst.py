# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, target, visited):
        if root == None: return
        
        if target - root.val in visited: 
            self.isPair = True
            return
        
        visited.add(root.val)
        self.helper(root.left, target, visited)
        self.helper(root.right, target, visited)
        
    
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.isPair = False
        visited = set()
        self.helper(root, k, visited)
        return self.isPair