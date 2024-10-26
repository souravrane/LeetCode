class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        size = float('inf')
        sumSoFar = 0
        left = 0
        for right in range(len(nums)):
            sumSoFar += nums[right]
            while sumSoFar >= target:
                size = min(size, right - left + 1)
                sumSoFar -= nums[left]
                left += 1
        
        return size if size < float('inf') else 0