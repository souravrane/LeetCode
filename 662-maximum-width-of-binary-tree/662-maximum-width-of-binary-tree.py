# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict, deque

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxWidth = 0
        currentLevel = deque([(root,1)])
        
        while currentLevel:
            
            s = len(currentLevel)
            maxWidth = max(maxWidth, currentLevel[-1][1] - currentLevel[0][1] + 1)

            for i in range(s):
                node,index = currentLevel.popleft()
                if node.left : currentLevel.append((node.left, 2*index))
                if node.right : currentLevel.append((node.right, 2*index+1))
            

        return maxWidth