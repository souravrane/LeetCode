# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrder(self, root, res):
        if root == None:
            return 
        
        self.inOrder(root.left, res)
        res.append(root.val)
        self.inOrder(root.right, res)
        
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        self.inOrder(root, res)
        return res[k-1]