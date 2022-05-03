class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        
        def check(posAns):
            partitions = 1
            currSum = 0
            for i in range(len(nums)):
                currSum += nums[i]
                if currSum > posAns:
                    currSum = nums[i]
                    partitions += 1
                    
            return partitions <= m 
        
        left = max(nums)
        right = sum(nums)
        ans = 0
        
        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans
    
    
    # 1   5    9
          