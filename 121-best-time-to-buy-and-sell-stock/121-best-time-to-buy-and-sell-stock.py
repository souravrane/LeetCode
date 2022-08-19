class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        futureMax = 0
        profit = 0
        
        for i in range(len(prices)-1,-1,-1):
            futureMax = max(futureMax, prices[i])
            profit = max(profit, futureMax - prices[i])
        
        return profit
        