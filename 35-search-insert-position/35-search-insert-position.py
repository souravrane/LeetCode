class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left , right = 0, len(nums)-1
        position = len(nums)
        while left <= right:
            mid = left + (right - left) // 2
            if(nums[mid] >= target):
                position = mid
                right = mid - 1
            else:
                left = mid + 1
        return position