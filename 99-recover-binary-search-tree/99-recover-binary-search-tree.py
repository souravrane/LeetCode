# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrder(self, root):
        if root == None:
            return
        
        self.inOrder(root.left)
        
        if self.prev != None and (self.prev.val > root.val):
            # violation found...
            
            if self.first == None:
                self.first = self.prev
                self.mid = root
            else:
                self.last = root
                return
        
        self.prev = root
        self.inOrder(root.right)

        
    def recoverTree(self, root: Optional[TreeNode], node1 = None, node2 = None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        self.first = self.mid = self.last = self.prev = None
        self.inOrder(root)
        
        if self.first and self.last:
            # both violations found
            self.first.val, self.last.val = self.last.val, self.first.val
            return 
        
        if self.first :
            # only first violation found
            self.first.val, self.mid.val = self.mid.val, self.first.val

    