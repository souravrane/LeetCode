class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = nums[0]
        count = 1
        for i in range(1, len(nums)):
            ele = nums[i]
            if ele == majority: count += 1
            else: count -= 1

            if count == 0:
                majority = nums[i + 1]
        return majority
        