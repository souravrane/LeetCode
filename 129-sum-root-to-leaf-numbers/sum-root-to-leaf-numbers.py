# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, path, result):
        if not root: return
        if not root.left and not root.right:
            path.append(str(root.val))
            result.append(int("".join(path)))
            path.pop()
            return
        
        path.append(str(root.val))
        self.helper(root.left, path, result)
        self.helper(root.right, path, result)
        path.pop()

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        path, result = [], []
        self.helper(root, path, result)
        return sum(result)
        