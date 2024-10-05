class Solution:
    def jump(self, nums: List[int]) -> int:
        hops = 0
        start, end = 0, 0

        while end < len(nums) - 1:
            hops += 1
            farthest = 0
            for i in range(start, end + 1):
                farthest = max(farthest, i + nums[i])
            start = end + 1
            end = farthest
        
        return hops

        