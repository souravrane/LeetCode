class Solution:
    def climbStairs(self, n: int, dp = {}) -> int:
        if n < 3: return n
        if n in dp: return dp[n]
        dp[n] = self.climbStairs(n-2) + self.climbStairs(n-1)
        return dp[n]
        
        