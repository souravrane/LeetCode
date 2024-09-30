class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = 1
        element = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == element:
                majority += 1
            else:
                majority -= 1
            
            if majority == 0:
                element = nums[i]
                majority = 1
        
        return element