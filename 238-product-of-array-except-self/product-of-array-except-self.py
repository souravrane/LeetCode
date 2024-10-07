class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]*len(nums)

        res = 1
        for i in range(len(nums)):
            ans[i] = res
            res *= nums[i]
        
        res = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= res
            res *= nums[i]
        
        return ans
        