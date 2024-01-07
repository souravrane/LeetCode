# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        maxSum = root.val
        reqLevel = 1

        dq = deque([root])
        level = 1
        while dq:
            levelSum = 0
            for i in range(len(dq)):
                node = dq.popleft()
                levelSum += node.val
                if node.left: dq.append(node.left)
                if node.right: dq.append(node.right)
            
            if levelSum > maxSum:
                maxSum = levelSum
                reqLevel = level

            level += 1
        return reqLevel

