class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if 0 not in nums: return len(nums) - 1
        longestOnes = 0
        for i in range(len(nums)):
            left, right = 0, 0
            if nums[i] == 0:
                j = i-1
                while j >= 0 and nums[j] == 1:
                    left += 1
                    j -= 1

                j = i + 1
                while j < len(nums) and nums[j] == 1:
                    right += 1
                    j += 1
                
                longestOnes = max(longestOnes, left + right)
        return longestOnes

        