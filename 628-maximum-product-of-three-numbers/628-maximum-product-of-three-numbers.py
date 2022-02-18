class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse = True)
        
        n1 = nums[0]*nums[1]*nums[2]
        n2 = nums[0]*nums[-1]*nums[-2]
        
        return max(n1,n2)
        
        