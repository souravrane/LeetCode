class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        h = {}
        # We check if the index is present if yes then check for abs(i-nums[i]) <= k
        # Then we update the index of nums[i] in the map.
        # We udpate the index everytime because if there was an index which satisfied the above condition then we would have returned True
        for i in range(len(nums)):
            if nums[i] in h:
                if abs(i-h[nums[i]]) <= k:
                    return True
            h[nums[i]] = i
            
        return False
        