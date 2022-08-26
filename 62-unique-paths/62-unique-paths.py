class Solution:
    def helper(self, m, n, x, y, dp):
        if x == m or y == n: return 0
        if x == m-1 and y == n-1: return 1
        
        if dp[x][y] != -1: return dp[x][y]
        dp[x][y] = self.helper(m,n,x+1,y,dp) + self.helper(m,n,x,y+1,dp)
        return dp[x][y]
    
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1]*n for _ in range(m)]
        return self.helper(m,n,0,0,dp)
        