class Solution:
    def helper(self, nums, index, cache):
        if index in cache: return cache[index]

        if index == len(nums) - 1: return 0
        if index > len(nums) - 1: return len(nums) - 1

        jumps = len(nums) - 1
        for i in range(1, nums[index]+1):
            jumps = min(jumps, 1 + self.helper(nums, index + i, cache))
        
        cache[index] = jumps
        return jumps

    def jump(self, nums: List[int]) -> int:
        return self.helper(nums, 0, dict())
        