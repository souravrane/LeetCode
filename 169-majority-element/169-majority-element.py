class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = 0
        count = 1
        
        for i in range(1,len(nums)):
            if nums[majority] == nums[i]:
                count += 1
            else:
                count -= 1
            
            if count == 0:
                majority = i+1
                count = 0
        
        return nums[majority]
        