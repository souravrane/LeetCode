class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        
        while j < len(nums):
            
            # swap condition
            if nums[i] == 0 and nums[j] != 0:
                nums[i],nums[j] = nums[j],nums[i]
            
            # when to increment i
            if nums[i] != 0:
                i += 1
            
            
            j += 1
            
                
        
            
        