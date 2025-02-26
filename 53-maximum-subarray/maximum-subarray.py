class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        maxSum = float('-inf')
        for i in range(len(nums)):
            curSum += nums[i]
            maxSum = max(maxSum, curSum)
            if curSum < 0:
                curSum = 0
            
        return maxSum


'''
maxSum = 6 , interval = [3,9]
cursum = 3
[-2,1,-3,4,-1,2,1,-5,4]
'''

        