# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int, runningSum = 0) -> bool:
        if root == None:
            return False
        
        newSum = runningSum + root.val
        
        if newSum == targetSum and root.left == None and root.right == None:
            return True
        
        return self.hasPathSum(root.left, targetSum, newSum) | self.hasPathSum(root.right, targetSum, newSum)
        
        