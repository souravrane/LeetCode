# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLeafSequence(self, root, seq):
        if not root: return seq
        if root.left == None and root.right == None: 
            seq.append(root.val)
            return seq
        self.getLeafSequence(root.left, seq)
        self.getLeafSequence(root.right, seq)
        return seq

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        tree1 = self.getLeafSequence(root1, [])
        tree2 = self.getLeafSequence(root2, [])
        print(tree1)
        if len(tree1) != len(tree2): return False
        for i in range(len(tree1)):
            if tree1[i] != tree2[i]: return False
        return True
