class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = defaultdict(int)
        for i in range(len(nums)):
            n = nums[i]
            if target - n in numMap: return [ numMap[target - n], i]
            numMap[n] = i
        return []
        