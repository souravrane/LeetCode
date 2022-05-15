# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum = 0
        
    def getMaxDepth(self,root, l):
        if root == None:
            return l
        
        left = self.getMaxDepth(root.left, l+1)
        right = self.getMaxDepth(root.right, l+1)
        
        return max(left,right)
    
    def getSum(self, root, l, maxDepth):
        if root == None:
            return
        
        if root.left == None and root.right == None and l+1 == maxDepth:
            self.sum += root.val
        
        self.getSum(root.left, l+1, maxDepth)
        self.getSum(root.right, l+1, maxDepth)

    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        maxDepth = self.getMaxDepth(root, 0)
        self.getSum(root, 0, maxDepth)
        return self.sum
        