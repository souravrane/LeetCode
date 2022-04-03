# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.total = 0
        
    def branchSums(self, node, runningNum):
        if node == None:
            return 
        
        newNum = (runningNum * 10) + node.val
        if node.right == None and node.left == None:
            self.total += newNum
        
        self.branchSums(node.left, newNum)
        self.branchSums(node.right, newNum)
        

        
    
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.branchSums(root, 0)
        return self.total
        