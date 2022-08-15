class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
        maxSum = float('-inf')
        
        curSum = 0
        for i in range(len(nums)):
            curSum += nums[i]
            maxSum = max(maxSum, curSum)
            curSum = max(curSum,0)
        
        return maxSum
        