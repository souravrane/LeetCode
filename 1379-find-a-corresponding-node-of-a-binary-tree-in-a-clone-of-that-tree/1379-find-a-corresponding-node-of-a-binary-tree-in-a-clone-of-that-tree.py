# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def helper(origRoot, cloneRoot):
            if origRoot == None:
                return None
            
            if origRoot == target:
                return cloneRoot
            
            return helper(origRoot.left, cloneRoot.left) or helper(origRoot.right, cloneRoot.right)

        
        
        return helper(original, cloned)
        
        