# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if root == None:
            return None
        
        '''
        Invalid node
        Ignore entire left subtree of this node
        and return the root of trimmed right subtree
        '''
        if root.val < low:
            return self.trimBST(root.right, low, high)
        
        '''
        Invalid node
        Ignore entire left subtree of this node
        and return the root of trimmed left subtree
        '''
        if root.val > high:
            return self.trimBST(root.left, low, high)
        
        '''
        The current node is valid.
        So trim the left subtree and assign it to its left child
        and trim the right subtree and assign it to its right child
        '''
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        
        return root
        