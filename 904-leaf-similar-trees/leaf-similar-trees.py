# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLeafSequence(self, root, seq):
        if root.left == None and root.right == None: 
            seq.append(root.val)
        if root.left: self.getLeafSequence(root.left, seq)
        if root.right: self.getLeafSequence(root.right, seq)
        return seq

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        tree1 = self.getLeafSequence(root1, [])
        tree2 = self.getLeafSequence(root2, [])
        return tree1 == tree2
