class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        start = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[start] = nums[i]
                start += 1
        
        for i in range(start, len(nums)):
            nums[i] = 0


            
            
            
            
        