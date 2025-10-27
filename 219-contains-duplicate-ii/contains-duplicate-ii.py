class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = defaultdict(int)
        for i in range(len(nums)):
            num = nums[i]
            if num in seen and i-seen[num] <= k: return True
            seen[num] = i
        return False
        