# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkSymmetry(self, p, q):
        if not p and not q: return True
        if not p or not q: return False
        if p.val != q.val: return False
        lst = self.checkSymmetry(p.left, q.right)
        rst = self.checkSymmetry(p.right, q.left)
        return lst and rst

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.checkSymmetry(root.left, root.right)