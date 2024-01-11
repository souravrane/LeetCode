# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def construct(self, pos, i, j, ino, x, y):
        if i > j: return None

        #create the root
        root = TreeNode(pos[j])

        # find root in ino
        idx = self.inorderMap[pos[j]]

        # create lst and rst
        left = self.construct(pos, i, j-(y-idx)-1, ino, x, idx-1)
        right = self.construct(pos, j-(y-idx), j-1, ino, idx+1, y) 

        root.left = left
        root.right = right
        return root

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        self.inorderMap = dict()
        for i,num in enumerate(inorder): self.inorderMap[num] = i
        return self.construct(postorder, 0, n-1, inorder, 0, n-1)