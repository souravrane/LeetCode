class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxOnes, zero = 0, 0
        start, end = 0, 0
        while end < len(nums):
            if nums[end] == 0:
                zero += 1
            
            while zero > k:
                if nums[start] == 0: zero -= 1
                start += 1

            maxOnes = max(maxOnes, end - start + 1)
            end += 1
        return maxOnes
            
            


            


