class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele = nums[0]
        count = 0
        for i in range(len(nums)):
            if nums[i] == ele: count += 1
            else : count -= 1

            if count == 0:
                ele = nums[i]
                count = 1
        
        return ele

        