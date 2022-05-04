class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        j = len(nums)-1
        operations = 0
        
        while i < j:
            s = nums[i] + nums[j]
            if s > k: j-= 1
            elif s < k: i += 1
            else:
                i += 1
                j -= 1
                operations += 1
        
        return operations