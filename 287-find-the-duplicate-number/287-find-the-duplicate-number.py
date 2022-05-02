class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def check(x):
            count = 0
            for i in nums:
                if i <= x: count += 1
            return count > x
        
        
        left = 1
        right = len(nums)
        ans = 0
        
        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans