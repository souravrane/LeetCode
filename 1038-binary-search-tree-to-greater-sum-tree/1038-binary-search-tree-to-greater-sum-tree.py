# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum = 0
        
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root == None:
            return 
        
        self.bstToGst(root.right)
        
        root.val = root.val + self.sum
        self.sum = root.val
        
        self.bstToGst(root.left)
        
        return root