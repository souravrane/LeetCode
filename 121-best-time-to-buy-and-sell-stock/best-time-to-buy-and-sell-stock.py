class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minBuySoFar = prices[0]
        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - minBuySoFar)
            minBuySoFar = min(minBuySoFar, prices[i])
        return profit
        