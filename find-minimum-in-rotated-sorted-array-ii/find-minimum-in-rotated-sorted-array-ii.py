class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        ans = float('inf')
        while left <= right:
            
            if nums[left] < nums[right]:
                ans = min(ans, nums[left])
                break
            
            mid = left + (right - left) // 2
            
            ans = min(ans, nums[mid])
            
            if nums[mid] < nums[right]:
                right = mid - 1
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right -= 1
        
        return ans