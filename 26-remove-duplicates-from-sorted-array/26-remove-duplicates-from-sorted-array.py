class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        for j in range(n):
            if nums[i] < nums[j]:
                nums[i+1] = nums[j]
                i += 1
            
            j += 1
        
        return (i + 1)