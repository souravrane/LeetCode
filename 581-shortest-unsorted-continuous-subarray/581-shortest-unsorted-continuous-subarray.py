class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums2 = sorted(nums)
        count = 0
        n = len(nums)
        
        if n == 1: return 0
        
        left = 0
        while left < n and nums[left] == nums2[left]: left += 1
            
        right = n-1
        while right > 0 and nums[right] == nums2[right]: right -= 1
        
        if left == n: return 0
        
        return right - left + 1
        