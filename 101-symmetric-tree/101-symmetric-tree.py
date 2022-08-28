# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, leftRoot, rightRoot):
        if leftRoot == None and rightRoot == None: return True
        if leftRoot == None or rightRoot == None: return False
        if leftRoot.val != rightRoot.val: return False

        return self.helper(leftRoot.left, rightRoot.right) and self.helper(leftRoot.right, rightRoot.left)
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root.left, root.right)
        