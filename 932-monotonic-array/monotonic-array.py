class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing, decreasing = True, True
        for i in range(1, len(nums)):
            if(nums[i-1] > nums[i]): increasing = False
            if(nums[i-1] < nums[i]): decreasing = False
        return increasing or decreasing