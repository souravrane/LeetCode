# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLeafSequence(self, root):
        if root.left == None and root.right == None: 
            self.temp.append(root.val)
        if root.left: self.getLeafSequence(root.left)
        if root.right: self.getLeafSequence(root.right)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.temp = []
        self.getLeafSequence(root1)
        self.tree1 = self.temp.copy()
        self.temp.clear()

        self.getLeafSequence(root2)
        self.tree2 = self.temp.copy()
        return self.tree1 == self.tree2
