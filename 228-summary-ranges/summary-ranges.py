class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = list()
        i = 0
        while i < len(nums):
            start = nums[i]

            while i + 1 < len(nums) and nums[i + 1] - nums[i] == 1:
                i += 1
            
            if start != nums[i]:
                result.append(f"{start}->{nums[i]}")
            else:
                result.append(f"{start}")
            
            i += 1
            
        return result