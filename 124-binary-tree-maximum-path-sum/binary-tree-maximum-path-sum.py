# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root):
        if not root: return 0        
        left_max_sum = self.helper(root.left)
        right_max_sum = self.helper(root.right)

        left_max_sum = max(left_max_sum, 0)
        right_max_sum = max(right_max_sum, 0)
        self.maxSum = max(self.maxSum , root.val + left_max_sum + right_max_sum)

        return root.val + max(left_max_sum, right_max_sum)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float('-inf')
        path = list()
        self.helper(root)
        return self.maxSum
        