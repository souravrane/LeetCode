class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero, nonZero = 0, 0
        while zero < len(nums) and nonZero < len(nums):
            while zero < len(nums) and nums[zero] != 0: zero += 1
            while nonZero < len(nums) and nums[nonZero] == 0: nonZero += 1
            if zero < len(nums) and nonZero < len(nums) and zero < nonZero:
                nums[zero], nums[nonZero] = nums[nonZero], nums[zero]
            else:
                nonZero += 1
            
            
            
        