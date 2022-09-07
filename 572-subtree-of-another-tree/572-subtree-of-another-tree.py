# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def stringifyTree(self, root):
        if root == None: return ["#"]
        lst = self.stringifyTree(root.left)
        rst = self.stringifyTree(root.right)
        return ["r" + str(root.val) + "c"] + lst + rst
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        tree = ''.join(self.stringifyTree(root))
        subTree = ''.join(self.stringifyTree(subRoot))
        return subTree in tree
        
        