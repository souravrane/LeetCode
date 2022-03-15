from functools import cmp_to_key

def compare(a,b):
    if a[0] > b[0]:
        return 1
    return -1

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals,key=cmp_to_key(compare))
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1],interval[1])
        
        return merged
        