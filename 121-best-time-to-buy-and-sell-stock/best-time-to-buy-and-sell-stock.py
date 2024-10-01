class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lowestSoFar = float('inf')
        for i in range(len(prices)):
            lowestSoFar = min(lowestSoFar, prices[i])
            profit = max(profit, prices[i] - lowestSoFar)
        return profit
          