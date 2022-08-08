# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def depth(self, root):
        if root == None: return 0
        
        lh = self.depth(root.left)
        rh = self.depth(root.right)
        
        self.diameter = max(self.diameter, lh + rh)
        return 1 + max(lh,rh)
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.depth(root)
        return self.diameter
        