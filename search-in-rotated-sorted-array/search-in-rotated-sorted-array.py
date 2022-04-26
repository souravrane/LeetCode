class Solution:
    def binarySearch(self, nums, target):
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            
            mid = left + ( right - left ) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1
        
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        shiftPoint = 0
        
        while left <= right:
            
            mid = left + ( right - left ) // 2
            
            if mid > 0 and nums[mid-1] > nums[mid] :
                shiftPoint = mid
                break
            
            if nums[0] > nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        
        if nums[shiftPoint] <= target and target <= nums[len(nums)-1]:
            ans = self.binarySearch(nums[shiftPoint:], target)  
            return -1 if ans == -1 else shiftPoint + ans
        
        return self.binarySearch(nums[:shiftPoint], target)
            
            
            