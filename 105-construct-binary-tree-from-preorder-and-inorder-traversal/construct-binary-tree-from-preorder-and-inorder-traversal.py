class Solution:
    def helper(self, pre, i, j, ino, x, y):
        if i > j: return None

        # create the root
        root = TreeNode(pre[i])
        
        # find the root rootIdx
        rootIdx = self.inMap[pre[i]]

        # create left and right subtrees
        left = self.helper(pre, i + 1, i + (rootIdx - x), ino, x, rootIdx - 1)
        right = self.helper(pre, i + (rootIdx - x) + 1, j, ino, rootIdx + 1, y)

        root.left = left
        root.right = right
        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        self.inMap = dict()
        for idx,num in enumerate(inorder): self.inMap[num] = idx
        return self.helper(preorder, 0, n-1, inorder, 0, n-1)