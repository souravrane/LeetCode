# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        h = defaultdict(int)
        
        def helper(node, l, h):
            if node == None:
                return
            
            helper(node.left, l+1, h)
            
            if node.left == None and node.right == None:
                h[l] += node.val
                        
            helper(node.right, l+1, h)
            
        
        helper(root,0,h)
        ans, level = root.val, 0
        for key in h:
            if key > level:
                level = key
                ans = h[key]

        return ans