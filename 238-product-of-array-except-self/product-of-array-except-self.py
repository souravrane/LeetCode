class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]*len(nums)
        for i in range(1, len(nums)):
            result[i] = result[i-1]*nums[i-1]

        suffixProd = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            result[i] = result[i]*suffixProd
            suffixProd *= nums[i]

        return result