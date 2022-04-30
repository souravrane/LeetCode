from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        h = Counter(nums1)
        res = []
        
        for i in range(len(nums2)):
            val = nums2[i]
            if h[val] > 0:
                res.append(val)
                h[val] -= 1
            
        return res
         