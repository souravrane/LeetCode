# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, targetSum, curSum):
        if not root: return False
        if not root.left and not root.right:
            if curSum + root.val == targetSum: return True
            return False

        lst = self.helper(root.left, targetSum, curSum + root.val)
        rst = self.helper(root.right, targetSum, curSum + root.val)
        return lst or rst

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        return self.helper(root, targetSum, 0)
        
        