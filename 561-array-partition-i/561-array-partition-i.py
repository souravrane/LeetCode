class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        res = 0
        # on observation we find that if we want to maximize the sum of min of pairs formed
        # We will have to sort them first, so that we end up choosing min of every consecutive pair that is formed.
        for i in range(0,len(nums),2):
            res += nums[i]
        return res
            