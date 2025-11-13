# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, postorder, i, j, inorder, x, y):
        if i > j: return None

        root = postorder[j]
        root_node = TreeNode(root)
        
        idx = self.inorder_idx[root]
        lst = self.helper(postorder, i, j-(y-idx)-1, inorder, x, idx-1)
        rst = self.helper(postorder, j-(y-idx), j-1, inorder, idx+1, y)

        root_node.left = lst
        root_node.right = rst
        return root_node

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.inorder_idx = dict()
        size = len(postorder)
        for k,v in enumerate(inorder):
            self.inorder_idx[v] = k
        return self.helper(postorder, 0, size-1, inorder, 0, size-1)
        