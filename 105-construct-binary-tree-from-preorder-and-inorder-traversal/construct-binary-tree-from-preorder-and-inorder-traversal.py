# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, pre, i, j, ino, x, y):
        if i > j: return None

        # create the root
        root = TreeNode(pre[i])
        
        # find the root rootIdx
        rootIdx = 0
        for _ in range(len(ino)):
            if ino[_] == pre[i]:
                rootIdx = _
                break

        # create left and right subtrees
        left = self.helper(pre, i + 1, i + (rootIdx - x), ino, x, rootIdx - 1)
        right = self.helper(pre, i + (rootIdx - x) + 1, j, ino, rootIdx + 1, y)

        root.left = left
        root.right = right
        return root



    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        return self.helper(preorder, 0, n-1, inorder, 0, n-1)