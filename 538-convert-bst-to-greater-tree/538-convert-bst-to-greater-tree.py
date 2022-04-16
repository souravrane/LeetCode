# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def newBST(self, root, sumSoFar):
        if root == None:
            return sumSoFar
        
        newSum = self.newBST(root.right, sumSoFar)
        
        root.val = root.val + newSum
        
        return self.newBST(root.left, root.val)
        
    
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        self.newBST(root,0)
        return root
        