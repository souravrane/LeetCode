# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode, maxSoFar = float('-inf')) -> int:
        foundGN = False
        if not root: return 0
        if root.val >= maxSoFar: foundGN = True
        leftGN = self.goodNodes(root.left, max(maxSoFar, root.val))
        rightGN = self.goodNodes(root.right, max(maxSoFar, root.val))
        if foundGN: return 1 + leftGN + rightGN
        return leftGN + rightGN