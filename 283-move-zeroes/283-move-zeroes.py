class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        for nonZero in range(len(nums)):
            if nums[zero] == 0 and nums[nonZero] != 0:
                nums[zero] , nums[nonZero] = nums[nonZero], nums[zero]
            
            if nums[zero] != 0: zero += 1
        
            
            
        