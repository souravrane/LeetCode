class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        r = len(obstacleGrid)
        c = len(obstacleGrid[0])
        
        dp = {}
        
        # recursive path calculator
        def path(i,j):
            if i == r-1 and j == c-1 and obstacleGrid[i][j] != 1:
                return 1
            
            if i == r or j == c or obstacleGrid[i][j] == 1:
                return 0
            
            if (i,j) in dp: return dp[(i,j)]
            
            p1 = path(i+1,j)
            p2 = path(i,j+1)
            dp[(i,j)] = p1+p2
            
            return dp[(i,j)]
        
        return path(0,0)