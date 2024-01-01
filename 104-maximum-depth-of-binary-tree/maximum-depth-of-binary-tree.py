# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None: return 0
        depth = 0
        level = deque([root])
        while level:
            for num in range(len(level)):
                node = level.popleft()
                if node.left: level.append(node.left)
                if node.right: level.append(node.right)
            depth += 1
        return depth

        
        