class Solution:
    def __init__(self):
        self.ans = 1
        
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        r = len(matrix)
        c = len(matrix[0])
        dp = {0:1}
        
        def validCell(i,j):
            if i - 1 >= 0 and matrix[i-1][j] > matrix[i][j]: return True
            if i + 1 < r and matrix[i+1][j] > matrix[i][j]: return True
            if j - 1 >= 0 and matrix[i][j-1] > matrix[i][j]: return True
            if j + 1 < c and matrix[i][j+1] > matrix[i][j]: return True
            return False
        
        def path(x, y , prev, stepsSoFar):
            if x < 0 or x == r or y == c or y < 0 or prev >= matrix[x][y]:
                return 0
            
            if (x,y) in dp: return dp[(x,y)]
            
            p1 = path(x+1,y,matrix[x][y], stepsSoFar + 1)
            p2 = path(x-1,y,matrix[x][y], stepsSoFar + 1)
            p3 = path(x,y+1,matrix[x][y], stepsSoFar + 1)
            p4 = path(x,y-1,matrix[x][y], stepsSoFar + 1)
            dp[(x,y)] = max(p1,p2,p3,p4) + 1
            return dp[(x,y)]
            
        
        for i in range(r):
            for j in range(c):
                if validCell(i,j): 
                    path(i,j,-1,0)
        
        return max(dp.values())
        