class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        maxPairSum = 0
        i,j = 0,len(nums)-1
        while i < j:
            maxPairSum = max(maxPairSum,nums[i]+nums[j])
            i += 1
            j -= 1
        return maxPairSum
            