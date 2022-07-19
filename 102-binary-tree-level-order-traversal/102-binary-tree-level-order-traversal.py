# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None: return []
        currentLevel = deque([root])
        res = []
        while currentLevel:
            size = len(currentLevel)
            level = []
            for i in range(size):
                node = currentLevel.popleft()
                level.append(node.val)
                
                if node.left: currentLevel.append(node.left)
                if node.right: currentLevel.append(node.right)
            
            res.append(level)
        return res
        
        