# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = TreeNode()
        self.cur = self.res
    
    
    def inOrder(self, root):
        if root == None: return
        
        self.inOrder(root.left)
        
        self.cur.right = root
        root.left = None
        self.cur = root
        
        self.inOrder(root.right)
        
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.inOrder(root)
        return self.res.right
        