# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root):
        if not root: return None

        leftTail = self.dfs(root.left)
        rightTail = self.dfs(root.right)

        if leftTail:
            leftTail.right = root.right
            root.right = root.left
        
        root.left = None
        return rightTail or leftTail or root

    def flatten(self, root: Optional[TreeNode]) -> None:
        self.dfs(root)

        