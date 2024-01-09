# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, lRoot, rRoot):
        if not lRoot and not rRoot: return True
        elif not lRoot or not rRoot: return False
        elif lRoot.val != rRoot.val: return False
        sym1 = self.helper(lRoot.left, rRoot.right)
        sym2 = self.helper(lRoot.right, rRoot.left)
        return sym1 & sym2


    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root.left, root.right)