class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, len(nums)-1
        count = 0

        while left < right:
            s = nums[left] + nums[right]
            if s < k: left += 1
            elif s > k: right -= 1
            else:
                count += 1
                left += 1
                right -= 1
        
        return count


        