class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = set()
        for i in range(len(nums)):
            num = nums[i]
            if (target - num) in visited: return [nums.index(target-num), i]
            visited.add(num)
        return []