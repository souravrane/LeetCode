# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], left = float('-inf'), right = float('inf')) -> bool:
        if root == None: return True
        if left >= root.val or root.val >= right: return False
        lst = self.isValidBST(root.left, left, root.val)
        rst = self.isValidBST(root.right, root.val, right)
        return lst and rst
    
            
        
        
        