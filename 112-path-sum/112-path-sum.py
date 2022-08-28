# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int, branchSum = 0) -> bool:
        if root == None: return False
        if branchSum + root.val == targetSum and not root.left and not root.right: return True
        
        lst = self.hasPathSum(root.left, targetSum, branchSum + root.val) 
        rst = self.hasPathSum(root.right, targetSum, branchSum + root.val)
        return lst or rst
        