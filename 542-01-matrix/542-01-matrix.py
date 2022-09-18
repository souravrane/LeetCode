from collections import deque
from copy import deepcopy

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        result = deepcopy(mat)
        visited = set()
        level = deque([])
        r,c = len(mat), len(mat[0])
        
        for i in range(r):
            for j in range(c):
                if mat[i][j] == 0: 
                    level.append((i,j))
                    visited.add((i,j))
                    
        
        def isValid(x,y):
            return (x >= 0 and x < r) and (y >= 0 and y < c) and (x,y) not in visited 
        
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        
        distance = 1
        while level:
            size = len(level)
            for i in range(size):
                x,y = level.popleft()
                for k in range(4):
                    newX = x + dx[k]
                    newY = y + dy[k]
                    if isValid(newX, newY):
                        level.append((newX, newY))
                        if mat[newX][newY] == 1: result[newX][newY] = distance
                        visited.add((newX,newY))
            
            distance += 1
        
        return result