# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int, currentSum = 0) -> bool:
        if not root: return False
        if not root.left and not root.right and currentSum + root.val == targetSum: return True
        
        lst = self.hasPathSum(root.left, targetSum, currentSum + root.val)
        rst = self.hasPathSum(root.right, targetSum, currentSum + root.val)

        return lst or rst