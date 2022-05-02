class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        
        def check(mid):
            totalPairs = 0
            j = 1
            for i in range(len(nums)):        
                while j < len(nums) and nums[j] - nums[i] <= mid:
                    j += 1
                totalPairs += (j - i - 1)
            
            return totalPairs >= k
                
                
        nums.sort()
        left = 0
        right = nums[-1] - nums[0]
        ans = 0
        
        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans