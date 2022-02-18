class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # move all the 0s to the left
        l,r = 0,len(nums)-1
        while l < r:
            if nums[l] == 0:
                l += 1
            elif nums[r] != 0:
                r -= 1
            
            if nums[l] != 0 and nums[r] == 0:
                nums[l],nums[r] = nums[r],nums[l]
                
        # move all the 2s to the right
        l,r = 0,len(nums)-1
        while l < r:
            if nums[r] == 2:
                r -= 1
            elif nums[l] != 2:
                l += 1
            
            if nums[r] != 2 and nums[l] == 2:
                nums[l],nums[r] = nums[r],nums[l]
        
        
            
                   
                
        
    
        
        