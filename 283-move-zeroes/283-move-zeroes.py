class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z = 0
        nz = 0
        
        while True:
            while nz < len(nums) and nums[nz] == 0: nz += 1
            while z < len(nums) and nums[z] != 0: z += 1
            if z == len(nums) or nz == len(nums): break
            if z < nz:
                nums[nz], nums[z] = nums[z], nums[nz]
            else:
                nz += 1
                
            
                
        
        