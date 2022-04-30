class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        ans = -1
        while left <= right:
            
            mid = left + (right - left) // 2
            
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                ans = mid
                right = mid - 1
                
        return nums[ans]