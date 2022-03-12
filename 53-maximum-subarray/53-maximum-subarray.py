class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        runningSum = nums[0]
        
        maxSum = nums[0]
        
        n = len(nums)
        for i in range(1,n):
            if runningSum + nums[i] >= nums[i]:
                runningSum += nums[i]
            else:
                runningSum = nums[i]
            maxSum = max(maxSum,runningSum)
        
        return maxSum
            
            