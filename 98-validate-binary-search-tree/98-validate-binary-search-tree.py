# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isValidBST(self, root: Optional[TreeNode], leftBoundary = float('-inf'), rightBoundary = float('inf')) -> bool:
        if root == None: return True
        if root.val <= leftBoundary or root.val >= rightBoundary: return False
        
        lst = self.isValidBST(root.left, leftBoundary, root.val)
        rst = self.isValidBST(root.right, root.val, rightBoundary)
        return lst & rst
        
