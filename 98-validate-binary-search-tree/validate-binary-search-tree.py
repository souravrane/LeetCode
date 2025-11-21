# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], left_boundary = float('-inf'), right_boundary = float('inf')) -> bool:
        if not root: return True

        val = root.val
        if val <= left_boundary or val >= right_boundary: return False

        lst = self.isValidBST(root.left, left_boundary, root.val)
        rst = self.isValidBST(root.right, root.val, right_boundary)

        return lst and rst 
        