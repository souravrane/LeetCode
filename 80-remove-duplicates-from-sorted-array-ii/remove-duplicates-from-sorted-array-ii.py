class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 2
        for i in range(2,len(nums)):
            if (nums[i] == nums[index-1] and nums[i] != nums[index-2]) or (nums[i] > nums[i-1]):
                nums[index] = nums[i]
                index += 1
        return index
            
        