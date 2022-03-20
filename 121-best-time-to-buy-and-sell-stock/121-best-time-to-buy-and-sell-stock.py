class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxHigh = prices[-1]
        profit = 0
        for i in range(len(prices)-2,-1,-1):
            if prices[i] > maxHigh:
                maxHigh = prices[i]
            else:
                profit = max(profit,maxHigh - prices[i])
        return profit
        