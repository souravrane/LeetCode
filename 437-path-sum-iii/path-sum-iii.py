from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, targetSum, curSum, cache):
        if not root: 
            return
        
        # check for the targetSum & add the sum to map
        curSum += root.val
        self.ans += cache[curSum - targetSum]
        cache[curSum] += 1

        left = self.solve(root.left, targetSum, curSum, cache)
        right = self.solve(root.right, targetSum, curSum, cache)
        
        # remove the sum
        cache[curSum] -= 1

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.ans = 0
        cache = defaultdict(int)
        cache[0] = 1
        self.solve(root, targetSum, 0, cache)
        return self.ans
        

