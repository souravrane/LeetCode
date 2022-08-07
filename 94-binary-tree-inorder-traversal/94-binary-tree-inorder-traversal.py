# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        cur = root
        
        # L data R
        while cur != None:
            # If there is no Left subtree.
            if cur.left == None:
                res.append(cur.val)
                cur = cur.right
                
            else:
                
                temp = cur.left
                while temp.right != None and temp.right != cur:
                    temp = temp.right
                
                # If temp.right is NULL
                if temp.right == None:
                    temp.right = cur 
                    cur = cur.left 
                    
                else:
                # If temp.right is already visited !
                    temp.right = None
                    res.append(cur.val)
                    cur = cur.right
        
        return res