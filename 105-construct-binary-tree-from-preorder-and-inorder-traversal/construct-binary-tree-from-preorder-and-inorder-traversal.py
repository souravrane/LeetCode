# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_idx_in_inorder(self, val):
        return self.inorder_map[val]

    def helper(self, preorder, ps, pe, inorder, ins, ine):
        if ps > pe: return None
        
        root = TreeNode(preorder[ps])
        
        i = self.get_idx_in_inorder(root.val)

        lst = self.helper(preorder, ps + 1, ps + (i - ins), inorder, ins, i - 1)
        rst = self.helper(preorder, ps + (i - ins) + 1, pe, inorder, i + 1, ine)

        root.left = lst
        root.right = rst
        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        size = len(preorder)
        self.inorder_map = dict()
        for idx, val in enumerate(inorder): self.inorder_map[val] = idx
        return self.helper(preorder, 0, size - 1, inorder, 0, size - 1)

        