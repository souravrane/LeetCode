# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque, defaultdict

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        currentLevel = deque([(root,0)])
        dMap = defaultdict(list)
        minn, maxx = float('inf'), float('-inf')
        
        while currentLevel:
            size = len(currentLevel)
            temp = defaultdict(list)
            
            for i in range(size):
                node,d = currentLevel.popleft()
                temp[d].append(node.val)

                minn = min(minn,d)
                maxx = max(maxx,d)

                if node.left: currentLevel.append((node.left,d-1))
                if node.right: currentLevel.append((node.right,d+1))
            
            for key in temp:
                if len(temp[key]) > 1: temp[key] = sorted(temp[key])
                dMap[key] += temp[key]
                
        
        vTraversal = []
        for key in range(minn,maxx+1):
            if key in dMap:
                vTraversal.append(dMap[key])
        
        return vTraversal
        
        

        