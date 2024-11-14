class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indexMap = defaultdict(list)
        for i in range(len(nums)):
            val = nums[i]
            indexMap[val].append(i)
            if len(indexMap[val]) > 1 and indexMap[val][-1] -  indexMap[val][-2] <= k: return True
        return False
            
            
        