class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minSoFar = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - minSoFar)
            minSoFar = min(minSoFar, prices[i])
        return profit


        