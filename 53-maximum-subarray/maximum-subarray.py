class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        runningSum = 0
        for num in nums:
            runningSum += num
            maxSum = max(maxSum, runningSum)
            if runningSum < 0: runningSum = 0
        return maxSum
        