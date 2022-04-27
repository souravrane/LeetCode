class Solution:
    def firstOccurance(self, nums, target):
        left = 0
        right = len(nums) - 1
        ans = -1
        
        while left <= right:
            
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                ans = mid
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return ans
    
    def lastOccurance(self, nums, target):
        left = 0
        right = len(nums) - 1
        ans = -1
        
        while left <= right:
            
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                ans = mid
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return ans
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.firstOccurance(nums, target)
        last = self.lastOccurance(nums, target)
        return [first, last]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        