class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        curSum = 0
        totalSum = sum(nums)
        
        for i in range(len(nums)):
            left = curSum
            right = totalSum - curSum - nums[i]
            if left == right:
                return i 
            
            curSum += nums[i]
        return -1
        