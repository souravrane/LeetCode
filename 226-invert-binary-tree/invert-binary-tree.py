# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return

        lst = self.invertTree(root.left)
        rst = self.invertTree(root.right)

        root.right = lst
        root.left = rst
        return root
        