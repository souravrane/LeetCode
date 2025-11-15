# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        lst = self.get_left_level(root)
        rst = self.get_right_level(root)

        if lst == rst:
            return pow(2, lst) - 1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
    
    def get_left_level(self, root):
        count = 0
        while root:
            count += 1
            root = root.left
        return count
    
    def get_right_level(self, root):
        count = 0
        while root:
            count += 1
            root = root.right
        return count
        