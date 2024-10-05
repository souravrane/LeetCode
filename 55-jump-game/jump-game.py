class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end = len(nums) - 1
        for i in range(len(nums)-2, -1, -1):
            distanceToEnd = end - i
            if nums[i] >= distanceToEnd: end = i
        return True if end == 0 else False
