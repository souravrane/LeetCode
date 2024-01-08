# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getInSuc(self, root):
        cur = root.right
        while cur.left: cur = cur.left
        return cur

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return root
        
        if root.val == key:
            if not root.right and not root.left: return None
            if not root.right or not root.left:
                if not root.right: return root.left
                else: return root.right
            else:
                inSuc = self.getInSuc(root)
                root.val = inSuc.val
                root.right = self.deleteNode(root.right, inSuc.val)
        
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)
        return root
        