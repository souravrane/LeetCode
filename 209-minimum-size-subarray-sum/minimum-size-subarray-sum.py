class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curSum, minSize = 0, len(nums) + 1
        start = 0
        for end in range(len(nums)):
            curSum += nums[end]

            while curSum >= target:
                minSize = min(minSize, end - start + 1)
                curSum -= nums[start]
                start += 1
            
        return minSize if minSize <= len(nums) else 0
        